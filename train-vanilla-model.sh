LANG_F=id
LANG_E=en
LANG_NOT_EN=id
BASEDIR=/home/liling/BPPT_CORPUS/
CORPUS=${BASEDIR}/corpus.tok/train-clean
DEV_F=${BASEDIR}/corpus.tok/dev.${LANG_F} 
DEV_E=${BASEDIR}/corpus.tok/dev.${LANG_E} 
TEST=${BASEDIR}/corpus.tok/test.${LANG_F} 
REF=${BASEDIR}/corpus.tok/test.${LANG_E} 

LOGFILE=phrase-${LANG_F}${LANG_E}.log

LM_ORDER=5
JOBS=10 

MOSES_SCRIPT=/home/liling/mosesdecoder/scripts/ 
MOSES_BIN_DIR=/home/liling/mosesdecoder/bin/
EXT_BIN_DIR=/home/liling/moses-training-tools/

WORK_DIR=work.${LANG_F}-${LANG_E} 
TRAINING_DIR=${WORK_DIR}/training 
MODEL_DIR=${WORK_DIR}/training/model/

mkdir phrasemodel
cd phrasemodel
mkdir -p ${TRAINING_DIR}

# Build Language model
LM_ARPA=‘pwd‘/${TRAINING_DIR}/lm/lm.${LANG_E}.arpa.gz
LM_FILE=‘pwd‘/${TRAINING_DIR}/lm/lm.${LANG_E}.kenlm

${MOSES_BIN_DIR}/lmplz --order ${LM_ORDER} -S 80% -T /tmp \
< ${CORPUS_LM}.${LANG_E} | gzip > ${LM_ARPA}

${MOSES_BIN_DIR}/build_binary trie -a 22 -b 8 -q 8 ${LM_ARPA} ${LM_FILE}

echo "START training @ $(date)" >> ${LOGFILE}

${MOSES_SCRIPT}/training/train-model-10c.perl \
  --root-dir `pwd`/${TRAINING_DIR} \
  --model-dir `pwd`/${MODEL_DIR} \
  --corpus ${CORPUS} \
  --external-bin-dir ${EXT_BIN_DIR} \
  --mgiza -mgiza-cpus 10 \
  --f ${LANG_F} \
  --e ${LANG_E} \
  --parallel \
  --alignment grow-diag-final-and \
  --reordering msd-bidirectional-fe \
  --score-options "--GoodTuring" \
  --lm 0:${LM_ORDER}:${LM_FILE}:8 \
  --cores ${JOBS} \
  --sort-buffer-size 10G \
  --parallel \
  >& ${TRAINING_DIR}/training_TM.log

echo "START filtering for tuning @ $(date)" >> ${LOGFILE}

${MOSES_SCRIPT}/training/filter-model-given-input.pl \
  ${MODEL_DIR}.filtered/dev \
  ${MODEL_DIR}/moses.ini \
  ${DEV_F} \
  -Binarizer ${MOSES_BIN_DIR}/processPhraseTableMin ${MOSES_BIN_DIR}/processLexicalTableMin \
  -threads ${JOBS} 

mkdir -p ${WORK_DIR}/tuning


echo "START MERT tuning @ $(date)" >> ${LOGFILE}

${MOSES_SCRIPT}/training/mert-moses.pl \
  ${DEV_F} \
  ${DEV_E} \
  ${MOSES_BIN_DIR}/moses \
  `pwd`/${MODEL_DIR}.filtered/dev/moses.ini \
  --mertdir ${MOSES_BIN_DIR} \
  --working-dir `pwd`/${WORK_DIR}/tuning/mert \
  --threads ${JOBS} \
  --decoder-flags "-threads ${JOBS} -distortion-limit 6" \
  --predictable-seeds \
  >& ${WORK_DIR}/tuning/mert.log 
  
echo "START substitue weight @ $(date)" >> ${LOGFILE}

perl ${MOSES_SCRIPT}/ems/support/substitute-weights.perl \
  ${MODEL_DIR}/moses.ini \
  ${WORK_DIR}/tuning/mert/moses.ini \
  ${MODEL_DIR}/moses-tuned.ini 


OUTPUT_DIR=${WORK_DIR}/output 
mkdir ${OUTPUT_DIR} 

echo "START filtering for test @ $(date)" >> ${LOGFILE}

${MOSES_SCRIPT}/training/filter-model-given-input.pl \
  ${MODEL_DIR}.filtered/test \
  ${MODEL_DIR}/moses-tuned.ini \
  ${TEST} \
  -Binarizer ${MOSES_BIN_DIR}/processPhraseTableMin ${MOSES_BIN_DIR}/processLexicalTableMin \
  -threads ${JOBS} 

echo "START decoding test @ $(date)" >> ${LOGFILE}

outfile=${OUTPUT_DIR}/test.out 

${MOSES_BIN_DIR}/moses -config ${MODEL_DIR}.filtered/test/moses.ini -threads ${JOBS} < ${TEST} > ${outfile} 2> ${outfile}.log 

${MOSES_SCRIPT}/recaser/detruecase.perl < ${outfile} > ${outfile}.tok 

${MOSES_SCRIPT}/tokenizer/detokenizer.perl -l ${LANG_E} < ${outfile}.tok > ${outfile}.detok 

echo "FINISH @ $(date)" >> ${LOGFILE}




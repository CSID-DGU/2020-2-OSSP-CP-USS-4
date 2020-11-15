#-*-coding:utf-8-*-
import tensorflow as tf

# tf.app.flags.DEFINE_string('f', '', 'kernel') # 주피터에서 커널에 전달하기 위한 프래그 방법
tf.app.flags.DEFINE_integer('batch_size', 64, 'batch size') # 배치 크기
tf.app.flags.DEFINE_integer('train_steps', 20000, 'train steps') # 학습 에폭
tf.app.flags.DEFINE_float('dropout_width', 0.8, 'dropout width') # 드롭아웃 크기
tf.app.flags.DEFINE_integer('layer_size', 1, 'layer size') # 멀티 레이어 크기(multi rnn)
tf.app.flags.DEFINE_integer('hidden_size', 128, 'weights size') # 가중치 크기
tf.app.flags.DEFINE_float('learning_rate', 1e-3, 'learning rate') # 학습률
tf.app.flags.DEFINE_float('teacher_forcing_rate', 0.7, 'teacher forcing rate') # 학습 시 디코더 인풋 정답 지원율
tf.app.flags.DEFINE_string('data_path', 'C:/Users/user/Desktop/B-version/data_in/ChatBotData.csv', 'data path') # 데이터 위치
tf.app.flags.DEFINE_string('vocabulary_path', 'C:/Users/user/Desktop/B-version/data_out/vocabularydata.voc', 'vocabulary path') # 사전 위치
tf.app.flags.DEFINE_string('check_point_path', 'C:/Users/user/Desktop/B-version/data_out/check_point', 'check point path') # 체크포인트 위치
tf.app.flags.DEFINE_string('save_model_path', 'C:/Users/user/Desktop/B-version/data_out', 'save model') # 모델 저장 경로
tf.app.flags.DEFINE_integer('shuffle_seek', 1000, 'shuffle random seek') # 셔플 시드 값
tf.app.flags.DEFINE_integer('max_sequence_length', 25, 'max sequence length') # 시퀀스 길이
tf.app.flags.DEFINE_integer('embedding_size', 128, 'embedding size') # 임베딩 크기
tf.app.flags.DEFINE_boolean('embedding', True, 'Use Embedding flag') # 임베딩 여부 설정
tf.app.flags.DEFINE_boolean('multilayer', True, 'Use Multi RNN Cell') # 멀티 RNN 여부
tf.app.flags.DEFINE_boolean('attention', True, 'Use Attention') # 어텐션 사용 여부
tf.app.flags.DEFINE_boolean('teacher_forcing', True, 'Use Teacher Forcing') # 학습 시 디코더 인풋 정답 지원여부
tf.app.flags.DEFINE_boolean('tokenize_as_morph', False, 'set morph tokenize') # 형태소에 따른 토크나이징 사용 여부 # 수정
tf.app.flags.DEFINE_boolean('serving', False, 'Use Serving') # 서빙 기능 지원여부 # 수정
tf.app.flags.DEFINE_boolean('loss_mask', False, 'Use loss mask') # PAD에 대한 마스크를 통한 loss 제한 # 수정


# Define FLAGS
DEFINES = tf.app.flags.FLAGS

import tensorflow as tf
import model as ml
import data
import numpy as np
import os
import sys


from configs import DEFINES

DATA_OUT_PATH = './data_out/' # 이 코드가 책에는 이렇게만 나와있는데 이렇게만 해도 되는지???

# Serving 기능을 위한 serving 함수를 구성
def serving_input_receiver_fn():
    receiver_tensor = {'input': tf.placeholder(dtype=tf.int32, shape=[None,
    DEFINES.max_sequence_length]),
    'output': tf.placeholder(dtype=tf.int32, shape=[None,
    DEFINES.max_sequence_length])}
    features = {key: tensor for key, tensor in receiver_tensor.items()}
    return tf.estimator.export.ServingInputReceiver(features, receiver_tensor)

def main(self):
    data_out_path = os.path.join(os.getcwd(), DATA_OUT_PATH)
    os.makedirs(data_out_path, exist_ok=True)
    # 데이터를 통한  사전 구성
    char2idx, idx2char, vocabulary_length = data.load_vocabulary()
    # 훈련 데이터와 평가 데이터를 가져옴
    train_input, train_label, eval_input, eval_label = data.load_data()

    # 훈련셋 인코딩을 만듦
    train_input_enc, train_input_enc_length = data.enc_processing(train_input, char2idx)
    # 훈련셋 디코딩 출력 부분을 만듦
    train_target_dec, train_target_dec_length = data.dec_target_processing(train_label, char2idx)

    # 평가셋 인코딩을 만듦
    eval_input_enc, eval_input_enc_length = data.enc_processing(eval_input, char2idx)
    # 평가셋 디코딩 출력 부분을 만듦
    eval_target_dec, _ = data.dec_target_processing(eval_label, char2idx)

    # 현재 경로인 './' 하부에
    # 체크포인트를 저장한 디렉토리를 설정
    check_point_path = os.path.join(os.getcwd(), DEFINES.check_point_path)
    save_model_path = os.path.join(os.getcwd(), DEFINES.save_model_path)
    # 디렉터리를 만드는 함수이며 두 번째 인자인 exist_ok가
    # True이면 디렉터리가 이미 존재해도 OSError가 발생하지 않음
    # exist_ok가 False이면 이미 존재할 경우 OSError가 발생
    os.makedirs(check_point_path, exist_ok=True)
    os.makedirs(save_model_path, exist_ok=True)

    # 에스티메이터를 구성
    classifier = tf.estimator.Estimator(
        model_fn=ml.Model, # 모델 등록 # 수정
        model_dir=DEFINES.check_point_path, # 체크포인트의 위치 등록
        params={ # 모델 쪽으로 파라미터를 전달
            'hidden_size': DEFINES.hidden_size,  # 가중치 크기
            'layer_size': DEFINES.layer_size, # 멀티 레이어 층 개수
            'learning_rate': DEFINES.learning_rate,  # 학습률 설정
            'teacher_forcing_rate': DEFINES.teacher_forcing_rate, # 학습 시 디코더
            # 인풋 정답 지원율 설정
            'vocabulary_length': vocabulary_length, # 딕셔너리 크기
            'embedding_size': DEFINES.embedding_size, # 임베딩 크기
            'embedding': DEFINES.embedding, # 임베딩 사용 여부
            'multilayer': DEFINES.multilayer, # 멀티 레이어 사용 여부
            'attention': DEFINES.attention, # 어텐션 지원 여부
            'teacher_forcing': DEFINES.teacher_forcing, # 학습 시 디코더 인풋 정답 지원 여부
            'loss_mask': DEFINES.loss_mask, # PAD에 대한 마스크를 통한 loss를 제한
            'serving': DEFINES.serving # 모델 저장 및 serving 여부 설정
        })

    # 학습 실행
    classifier.train(input_fn=lambda:data.train_input_fn(
        train_input_enc, train_target_dec_length, train_target_dec, DEFINES.batch_size),
    steps=DEFINES.train_steps)
    # 서빙 기능 여부에 따라 모델을 save
    if DEFINES.serving == True:
        save_model_path = classifier.export_savedmodel(export_dir_base=
        DEFINES.save_model_path,
        serving_input_receiver_fn=serving_input_receiver_fn)

    # 평가 실행
    eval_result = classifier.evaluate(input_fn=lambda:data.eval_input_fn(
        eval_input_enc, eval_target_dec, DEFINES.batch_size))
    print('\nEVAL set accuracy: {accuracy:0.3f}\n'.format(**eval_result))

if __name__ == '__main__':
    tf.logging.set_verbosity(tf.logging.INFO)
    tf.app.run(main)

tf.logging.set_verbosity

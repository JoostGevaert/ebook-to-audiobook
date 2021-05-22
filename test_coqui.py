import os
import subprocess

en_models = [
    'tts_models/en/ek1/tacotron2',
    'tts_models/en/ljspeech/tacotron2-DDC',
    'tts_models/en/ljspeech/glow-tts',
    'tts_models/en/ljspeech/tacotron2-DCA',
    'tts_models/en/ljspeech/speedy-speech-wn',
    'tts_models/en/sam/tacotron-DDC',
    # 'vocoder_models/en/ek1/wavegrad',
    # 'vocoder_models/en/ljspeech/multiband-melgan',
    # 'vocoder_models/en/ljspeech/hifigan_v2',
    # 'vocoder_models/en/vctk/hifigan_v2',
    # 'vocoder_models/en/sam/hifigan_v2'
]
for model in en_models:
    model_type = model.split('/')[-1]
    text = f'Hello, I am an English text-to-speech engine built with {model_type}. Do you think I sound like a robot? How would you like me to read the book Biomimicry in Architecture to you?'
    output_path = os.path.join('.', 'output', f'{model_type}.wav')
    # subprocess.run(
    print(
        ' '.join([
            'tts',
            f'--text "{text}"',
            f'--model_name "{model}"',
            f'--out_path {output_path}'
        ])
    )

text = 'Hola, soy una macina que convierte texto en una voz natural. Construyeron mi voz con tacotron2-DDC. Crees que sueno como un robot? Te gustaría si te leyese el libro Biomimicry in Architecture?'
model = "tts_models/es/mai/tacotron2-DDC"
output_path = os.path.join('.', 'output', 'es_tacotron2-DDC.wav')
# subprocess.run(
print(
    ' '.join([
        'tts',
        f'--text "{text}"',
        f'--model_name "{model}"',
        f'--out_path {output_path}'
    ])
)

text = 'Hoi, ik ben een machine die tekst omzet in een natuurlijke stem. Ze bouwden mijn stem met tacotron2-DDC. Denk je dat ik als een robot klink? Zou je het leuk vinden als ik je het boek Biomimicry in Architecture voorlees?'
nl_models = "tts_models/nl/mai/tacotron2-DDC"
output_path = os.path.join('.', 'output', 'nl_tacotron2-DDC.wav')
# subprocess.run(
print(
    ' '.join([
        'tts',
        f'--text "{text}"',
        f'--model_name "{model}"',
        f'--out_path {output_path}'
    ])
)

de_models = [
    "tts_models/de/thorsten/tacotron2-DCA",
    # "vocoder_models/de/thorsten/wavegrad"
]



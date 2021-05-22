import re
import pyttsx3


engine = pyttsx3.init()
voices = engine.getProperty('voices')

voice_registry_keys_en = [
    r"HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-GB_HAZEL_11.0",
    r"HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_DAVID_11.0",
    r"HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0"
]

voice_registry_keys_de = r"HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_DE-DE_HEDDA_11.0"

voice_registry_keys_es = r"HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_ES-ES_HELENA_11.0"

for i, voice_key in enumerate(voice_registry_keys_en):
    name = re.split('_', voice_registry_keys_en[i])[-2]
    engine.setProperty('voice', voice_key)
    engine.say(f"Hello, my name is {name} and I speak English. Do you think I sound like a robot?")
    engine.runAndWait()

engine.setProperty('voice', voice_registry_keys_de)
engine.say("Guttentag, mein Name ist Hedda und ich spreche Deutsch. Denken Sie, dass ich wie ein Roboter klinke?")
engine.runAndWait()

engine.setProperty('voice', voice_registry_keys_es)
engine.setProperty('rate', 160)
engine.say("Hola, me llamo Helena y yo hablo español. Piensa usted que hablo como un robot?")
engine.runAndWait()
engine.save_to_file("Hola, me llamo Helena y yo hablo español. Piensa usted que hablo como un robot?", "test_es.mp3")
engine.runAndWait()
engine.stop()

# The voices below can be unlocked by following these instructions:
# https://winaero.com/unlock-extra-voices-windows-10/ 
# https://www.ghacks.net/2018/08/11/unlock-all-windows-10-tts-voices-system-wide-to-get-more-of-them/
extra_voice_registry_keys_en = [
    r"HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech_OneCore\Voices\Tokens\MSTTS_V110_enGB_GeorgeM",
    r"HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech_OneCore\Voices\Tokens\MSTTS_V110_enGB_HazelM",
    r"HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech_OneCore\Voices\Tokens\MSTTS_V110_enGB_SusanM",
    r"HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech_OneCore\Voices\Tokens\MSTTS_V110_enUS_DavidM",
    r"HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech_OneCore\CortanaVoices\Tokens\MSTTS_V110_enUS_EvaM",
    r"HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech_OneCore\Voices\Tokens\MSTTS_V110_enUS_MarkM",
    r"HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech_OneCore\Voices\Tokens\MSTTS_V110_enUS_ZiraM",
    r"HKEY_CLASSES_ROOT\Local Settings\Software\Microsoft\Windows\CurrentVersion\AppContainer\Storage\microsoft.windows.cortana_cw5n1h2txyewy\SOFTWARE\Microsoft\Speech_OneCore\Isolated\jWXZvMzcRxToSdOzNgXV_L3ZSrLDNbZuY5NZNWCCUd8\HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech_OneCore\Voices\Tokens\MSTTS_V110_enGB_SarahM"
]

extra_voice_registry_keys_es = [
    r"HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech_OneCore\Voices\Tokens\MSTTS_V110_esES_HelenaM",
    r"HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech_OneCore\Voices\Tokens\MSTTS_V110_esES_LauraM",
    r"HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech_OneCore\Voices\Tokens\MSTTS_V110_esES_PabloM",
    r"HKEY_CLASSES_ROOT\Local Settings\Software\Microsoft\Windows\CurrentVersion\AppContainer\Storage\microsoft.windows.cortana_cw5n1h2txyewy\SOFTWARE\Microsoft\Speech_OneCore\Isolated\jWXZvMzcRxToSdOzNgXV_L3ZSrLDNbZuY5NZNWCCUd8\HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech_OneCore\Voices\Tokens\MSTTS_V110_esES_AnaM"
]

extra_voice_registry_keys_nl = [
    r"HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech_OneCore\Voices\Tokens\MSTTS_V110_nlNL_Frank"
]

extra_voice_registry_keys_de = [
    r"HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech_OneCore\Voices\Tokens\MSTTS_V110_deDE_KatjaM",
    r"HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech_OneCore\Voices\Tokens\MSTTS_V110_deDE_HeddaM",
    r"HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech_OneCore\Voices\Tokens\MSTTS_V110_deDE_StefanM",
    r"HKEY_CLASSES_ROOT\Local Settings\Software\Microsoft\Windows\CurrentVersion\AppContainer\Storage\microsoft.windows.cortana_cw5n1h2txyewy\SOFTWARE\Microsoft\Speech_OneCore\Isolated\jWXZvMzcRxToSdOzNgXV_L3ZSrLDNbZuY5NZNWCCUd8\HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech_OneCore\Voices\Tokens\MSTTS_V110_deDE_KatjaCortanaM"
]

extra_voice_registry_keys_fr = [
    r"HKEY_CLASSES_ROOT\Local Settings\Software\Microsoft\Windows\CurrentVersion\AppContainer\Storage\microsoft.windows.cortana_cw5n1h2txyewy\SOFTWARE\Microsoft\Speech_OneCore\Isolated\jWXZvMzcRxToSdOzNgXV_L3ZSrLDNbZuY5NZNWCCUd8\HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech_OneCore\Voices\Tokens\MSTTS_V110_frFR_HortenseM",
    r"HKEY_CLASSES_ROOT\Local Settings\Software\Microsoft\Windows\CurrentVersion\AppContainer\Storage\microsoft.windows.cortana_cw5n1h2txyewy\SOFTWARE\Microsoft\Speech_OneCore\Isolated\jWXZvMzcRxToSdOzNgXV_L3ZSrLDNbZuY5NZNWCCUd8\HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech_OneCore\Voices\Tokens\MSTTS_V110_frFR_JulieM",
    r"HKEY_CLASSES_ROOT\Local Settings\Software\Microsoft\Windows\CurrentVersion\AppContainer\Storage\microsoft.windows.cortana_cw5n1h2txyewy\SOFTWARE\Microsoft\Speech_OneCore\Isolated\jWXZvMzcRxToSdOzNgXV_L3ZSrLDNbZuY5NZNWCCUd8\HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech_OneCore\Voices\Tokens\MSTTS_V110_frFR_NathalieM",
    r"HKEY_CLASSES_ROOT\Local Settings\Software\Microsoft\Windows\CurrentVersion\AppContainer\Storage\microsoft.windows.cortana_cw5n1h2txyewy\SOFTWARE\Microsoft\Speech_OneCore\Isolated\jWXZvMzcRxToSdOzNgXV_L3ZSrLDNbZuY5NZNWCCUd8\HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech_OneCore\Voices\Tokens\MSTTS_V110_frFR_PaulM"
]

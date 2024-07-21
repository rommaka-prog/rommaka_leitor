from gtts import gTTS

texto = "Siga a Hashtag no YouTube e no Instagram para não perder nada"
lingua = "pt"
tts = gTTS(texto, lang=lingua)
tts.save("audio.mp3")
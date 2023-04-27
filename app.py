# Imports used through the rest of the notebook.
import torch
import torchaudio
import torch.nn as nn
import torch.nn.functional as F

from tortoise.api import TextToSpeech
from tortoise.utils.audio import load_audio, load_voice, load_voices

def gen(voice, text, preset = "fast",temperature = .8):
    tts = TextToSpeech()

    voice_samples, conditioning_latents = load_voice(voice)
    gen = tts.tts_with_preset(text, voice_samples=voice_samples, conditioning_latents=conditioning_latents, preset=preset, temperature=temperature)

    filename = f"generated-{voice}.wav"
    torchaudio.save(filename, gen.squeeze(0).cpu(), 24000)
    return filename

import gradio as gr
import time
from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler
from telegram.ext import filters, CallbackContext  # استيراد filters بشكل صحيح
import requests

# تعريف النماذج من Hugging Face
Models = [
  "Yntec/pineappleAnimeMix",
  "Yntec/DucHaiten-Retro-Diffusers",
  "Yntec/edgeOfRealism",
  "Yntec/epiCPhotoGasm",
  "Yntec/RealLife",
  "Yntec/Paramount",
  "Yntec/fennPhoto",
  "Yntec/Analog",
  "Yntec/iffyMix",
  "Yntec/photoMovieXFinal",
  "Yntec/YiffyMix",
  "Yntec/aMovieX",
  "Yntec/AbsoluteReality",
  "Yntec/DreamWorksRemix",
  "Yntec/photoMovieX",
  "Yntec/photoMovieRealistic",
  "Yntec/nuipenimix",
  "Yntec/IdleFancy",
  "Yntec/IncredibleWorld2",
  "Yntec/makeitdoubleplz",
  "Yntec/FotoPhoto",
  "Yntec/Memento",
  "Yntec/InsaneRealisticCVAE",
  "Yntec/nuipenimix2",
  "Yntec/realistic-vision-v12",
  "Yntec/Gacha",
  "Yntec/animeSIXTYNINE",
  "Yntec/InfiniteLiberty",
  "Yntec/CyberRealistic",
  "Yntec/CinematicReality",
  "Yntec/EmeraldCity",
  "Yntec/Jackpot",
  "Yntec/SQUEE",
  "Yntec/AnythingV4-768",
  "Yntec/NyankoMotsiX",
  "Yntec/epiCCartoon",
  "Yntec/CuteFurry",
  "Yntec/AnythingV3-768",
  "Yntec/Deliberate2",
  "Yntec/Dreamshaper8",
  "Yntec/CinemaEros",
  "Yntec/Aurora",
  "Yntec/level4",
  "Yntec/Reliberate",
  "Yntec/aBagOfChips",
  "Yntec/sexyToons",
  "Yntec/GoFish",
  "Yntec/AnalogMadness4",
  "Yntec/ResidentCNZCartoon3D",
  "Yntec/epiCVision",
  "Yntec/epiCRealismVAE",
  "Yntec/Photosphere",
  "Yntec/IncredibleWorld",
  "Yntec/LiberteRedmond",
  "Yntec/Kitsch-In-Sync",
  "Yntec/NaughtyChildren",
  "Yntec/Genuine",
  "Yntec/IsThisArt",
  "Yntec/GimmeDatDing",
  "Yntec/Hassanim",
  "Yntec/Thriller",
  "Yntec/AnalogMadness",
  "Yntec/Based64",
  "Yntec/LehinaModel",
  "Yntec/DaintyMix",
  "Yntec/mixRealisticFantasy",
  "Yntec/526Mix",
  "Yntec/Paragon",
  "Yntec/Looking-Glass",
  "Yntec/Ninja-Diffusers",
  "Yntec/RetroLife",
  "Yntec/CutesyAnime",
  "Yntec/ChiliConCarne",
  "Yntec/elldrethSDreamMix",
  "Yntec/DucHaiten-AnyUnreal",
  "Yntec/Cheesecake",
  "Yntec/RealCartoon3D",
  "Yntec/Dreamsphere",
  "Yntec/aMovieTrend",
  "Yntec/UberRealisticLegacy",
  "Yntec/Luma",
  "Yntec/humu",
  "Yntec/Astro_-_-Gemu",
  "Yntec/MGM",
  "Yntec/GoldenEra",
  "Yntec/Stuff",
  "Yntec/a-ZovyaRemix",
  "Yntec/Noosphere_v3_CVAE",
  "Yntec/Atlas",
  "Yntec/StorybookRedmond",
  "Yntec/Lunar",
  "Yntec/dreamlike-photoreal-remix",
  "Yntec/animeTWO",
  "Yntec/InsaneM3U",
  "Yntec/a-ZovyaRPGV3VAE",
  "Yntec/incha_re_zoro",
  "Yntec/Nostalgic",
  "Yntec/Lyriel",
  "Yntec/RealRainbows",
  "Yntec/StableDiffusion768",
  "Yntec/EstheticRetroAnime",
  "Yntec/La-dee-dah-.-_",
  "Yntec/ElldrethsRetroMix",
  "Yntec/Splash",
  "Yntec/AbsoluteRemix",
  "Yntec/526",
  "Yntec/aPhotographicTrend",
  "Yntec/BeautyFool",
  "Yntec/animeSEXTILLION",
  "Yntec/LAMEanime",
  "Yntec/SinkOrSwim",
  "Yntec/LeyLines",
  "Yntec/GodMode",
  "Yntec/AsianMix",
  "Yntec/REV",
  "Yntec/a-ZovyaRPGArtistV2VAE",
  "Yntec/lamettaNightly",
  "Yntec/DucHaitenDarkside4",
  "Yntec/Dreamful3",
  "Yntec/mistoonAnime2",
  "Yntec/WoopWoopRemix",
  "Yntec/foto-assisted-diffusion",
  "Yntec/DreamLikeRemix",
  "Yntec/Deliberate",
  "Yntec/lamettaRemix",
  "Yntec/ChildrenStoriesAnime",
  "Yntec/GOLDFish",
  "Yntec/AgarthaChadstyle",
  "Yntec/Darkside",
  "Yntec/DreamWorks",
  "Yntec/AnythingRemix",
  "Yntec/Infinite80s",
  "Yntec/HellSKitchen",
  "Yntec/LunarLuma",
  "Yntec/Vintedois",
  "Yntec/Protogen",
  "Yntec/DreamFulV2",
  "Yntec/lametta",
  "Yntec/OrangeRemix",
  "Yntec/BabeBae",
  "Yntec/DeliberateRealisticWoop",
  "Yntec/DreamShaperRemix",
  "Yntec/DucHaitenAnime768",
  "Yntec/DucHaiten-FANCYxFANCY",
  "Yntec/MemeDiffusion",
  "Yntec/animeTEN",
  "Yntec/DeliberateRemix",
  "Yntec/BaronMix",
  "Yntec/vividicAnime",
  "Yntec/CetusRemix",
  "Yntec/Rainbowsphere",
  "Yntec/StolenDreams",
  "Yntec/MapleSyrup",
  "Yntec/OpenGenDiffusers",
  "Yntec/WesternAnimation",
  "Yntec/mistoonEmerald2",
  "Yntec/MangledMerge3_768",
  "Yntec/RadiantCinemagic",
  "Yntec/Dreamlike",
  "Yntec/ReVAnimated",
  "Yntec/iComixRemix",
  "Yntec/DreamAnything",
  "Yntec/HassanBlend12",
  "Yntec/C-.-_-.-Aravaggio",
  "Yntec/3Danimation",
  "Yntec/ChilloutMix",
  "Yntec/CrystalClear",
  "Yntec/GenerateMe",
  "Yntec/theallysMixIIIRevolutions",
  "Yntec/KIDSILLUSTRATIONS",
  "Yntec/IronCatFateToons",
  "Yntec/HassanBlend1512VAE",
  "Yntec/Abased",
  "Yntec/WoopWoopAnime",
  "Yntec/yabalMixTrue25D_v2_VAE",
  "Yntec/CrystalClearRemix",
  "Yntec/Tea",
  "Yntec/SCMix",
  "Yntec/GoodLife",
  "Yntec/QToriReloaded",
  "Yntec/Tantrum",
  "Yntec/HassanRemix",
  "Yntec/DeliShaper",
  "Yntec/DucHaitenClassicAnime768",
  "Yntec/Cetus",
  "Yntec/Toonify2",
  "Yntec/OpenLexica",
  "Yntec/HELLmix",
  "Yntec/Playground",
  "Yntec/elldrethSVividMix",
  "Yntec/Remedy",
  "Yntec/3DRendering",
  "Yntec/Reddit",
  "Yntec/BrainDance",
  "Yntec/Ambrosia",
  "Yntec/Yuzu",
  "Yntec/GalenaVAE",
  "Yntec/DreamWorld",
  "Yntec/ArcticFowl",
  "Yntec/PotaytoPotahto",
  "Yntec/GameAssetsDigitalUnitsCreationKit",
  "Yntec/ClassicEra",
  "Yntec/Citrus",
  "Yntec/Cryptids",
  "Yntec/3DKX2",
  "Yntec/Wonderland",
  "Yntec/Crystalwave",
  "Yntec/CartoonStyleClassic",
  "Yntec/SuperCuteRemix",
  "Yntec/theallysMixIIChurned",
  "Yntec/NeverExisted",
  "Yntec/samaritan3dCartoon2MVAE",
  "Yntec/NeverEndingDream768",
  "Yntec/NovelAIRemix",
  "Yntec/3DKX",
  "Yntec/BrandiMilne",
  "Yntec/NovelAI",
  "Yntec/Emoticons",
  "Yntec/SillySymphonies",
  "Yntec/KomowataHaruka",
  "Yntec/Cute",
  "Yntec/TheDarkNight",
  "Yntec/OpenNijiRemix",
  "Yntec/FantassifiedIcons",
  "Yntec/Dreamscapes_n_Dragonfire_v2"
]

model_functions = {}
model_idx = 1
for model_path in models:
    try:
        model_functions[model_idx] = gr.Interface.load(f"models/{model_path}", live=False, preprocess=True, postprocess=False)
    except Exception as error:
        def the_fn(txt):
            return None
        model_functions[model_idx] = gr.Interface(fn=the_fn, inputs=["text"], outputs=["image"])
    model_idx += 1

def send_it_idx(idx):
    def send_it_fn(prompt):
        output = (model_functions.get(idx) or model_functions.get(1))(prompt)
        return output
    return send_it_fn

# إنشاء البوت
updater = Updater("7865424971:AAF_Oe6lu8ZYAl5XIF1M6qU_8MK6GHWEll8", use_context=True)
dispatcher = updater.dispatcher

# دالة بدء البوت
def start(update, context):
    update.message.reply_text('مرحبا! أرسل لي أي نص وسيتم توليد صورة بناءً على النماذج!')

# دالة التعامل مع الرسائل النصية
def handle_message(update, context):
    prompt = update.message.text
    # قائمة الصور الناتجة من جميع النماذج
    images = []
    
    # توليد صورة من كل نموذج في القائمة
    for model_idx in range(1, len(models) + 1):
        generated_image = send_it_idx(model_idx)(prompt)
        
        # التحقق من أن الصورة تم توليدها
        if generated_image:
            images.append(generated_image[0])  # إضافة الصورة إلى القائمة
    
    # إرسال جميع الصور إلى المستخدم
    if images:
        for image in images:
            update.message.reply_photo(photo=image)
    else:
        update.message.reply_text('حدث خطأ في توليد الصور.')

# ربط البوت بالأوامر
dispatcher.add_handler(CommandHandler("start", start))
dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, handle_message))

# بدء البوت
updater.start_polling()
updater.idle()

# إعداد واجهة Gradio (إذا كنت تستخدمها في الخلفية)
with gr.Blocks() as my_interface:
    with gr.Column():
        primary_prompt = gr.Textbox(label="Prompt", value="")
        run = gr.Button("Run")
        sd_outputs = {}
        for model_path in models:
            sd_outputs[model_idx] = gr.Image(label=model_path)
            model_idx += 1

    # إضافة الأحداث
    run.click(send_it_idx(1), inputs=[primary_prompt], outputs=[sd_outputs[model_idx]])

my_interface.launch(share=True)

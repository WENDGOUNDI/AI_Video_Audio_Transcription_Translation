# AI Video Audio Transcription Translation
Most of the time after, joining an online discussion, course, mentoring, we would like to access the speech in order to summarize it, make notes or create subtitles. How can we achieve this aim via AI? The goal of this project is to create an AI based solution, taking as input a video or an audio file and extract the speech. The extracted speech can be later converted into one of the 107 languages proposed by the system.


# Dependencies:
 - PySimpleGui
 - Speech_Recognition
 - Moviepy
 - Pathlib
 - Deep_Translator
 - Os
 - Textract
 
 
 # Translation Requirements
  - Video file extension should be .avi or .mp4
  - Audio file extension should be .mp3 and .wav
 # Translation Requirements
  - Text file extension should be between .text, .doc or .docx
  - The number of characters is limitted to 5000 per operation.
  - The system can translate a given text into one or multiple languages at the same time. For multilanguage translation, align languages as follow: french,english,japanese.
  
  # Solution Interface
  For the scope of simplicity, we converted the scrip into a GUI. The main tab allows the app operation and the second one teach how to use it.
  
  ![interface_1](https://user-images.githubusercontent.com/48753146/202963005-95ad375a-5102-4207-8d57-ef4270f9b4ac.PNG)
  
  ![interface_2](https://user-images.githubusercontent.com/48753146/202963008-24e1bb57-ccb4-4438-8da9-89cd223a690c.PNG)
  
  # Extras
  When an operations is completed successfuly, we will be visualy notified by the app as below.
  ![completed_task](https://user-images.githubusercontent.com/48753146/202969181-c3d7f006-e033-42b8-a956-1756ee5cd4ea.PNG)
  
  ## List of languages supported for translation
  ![languages_list2](https://user-images.githubusercontent.com/48753146/202970873-d78d295e-71d2-4b6e-96e3-6ec880a5b908.PNG)


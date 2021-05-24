# Userge Plugin to apply different AI operations from deepai.org
# Author: Nageen (https://github.com/archie9211) (@archie9211)
# All rights reserved

import requests, os
from userge import userge, Message, Config
from userge.plugins.misc.download import url_download
from userge.plugins.misc.upload import upload_path
from pathlib import Path

DEEP_API_KEY = os.environ.get("DEEPAI_API")


@userge.on_cmd("colorize", about={
	'header' : "Colorize black and white images or videos using AI",
	'description' : "",
	'usage' : ".colorize reply_to_image"
	})
async def colorize(message: Message):
	if message.reply_to_message:
		await message.edit("Please wait while I colorize the given media")
		message_ = message.reply_to_message
		if message_.animation:
			await messgage.edit("Animated images are not supported")
			return
		dis = await message.client.download_media(message=message_,file_name=Config.DOWN_PATH)
		dis_loc = os.path.join(Config.DOWN_PATH, os.path.basename(dis))

		del_path = False
		if dis_loc:
			try:
				await message.edit(dis_loc)
				del_path = True
				r = requests.post(
					"https://api.deepai.org/api/colorizer",
					files={
					    'image': open(dis_loc, 'rb'),
					},
					headers={'api-key': DEEP_API_KEY}
					)
				image_res = r.json()["output_url"]

			except Exception as e_e:
				await message.err(str(e_e))
				return
			try:
				file_, _ = await url_download(message, image_res)
			except Exception as e_e:  # pylint: disable=broad-except
				await message.err(str(e_e))
				return
			string = Path(file_)
			await message.delete()
			await upload_path(message, string, del_path)
@userge.on_cmd("srgan", about={
	'header' : "Clarify images and enhance resolution without feature loss.",
	'description' : "",
	'usage' : ".srgan reply_to_image"
	})
async  def srgan(message: Message):
	if message.reply_to_message:
		await message.edit("Please wait while I enhance the given media")
		message_ = message.reply_to_message
		if message_.animation:
			await messgage.edit("Animated images are not supported")
			return
		dis = await message.client.download_media(message=message_,file_name=Config.DOWN_PATH)
		dis_loc = os.path.join(Config.DOWN_PATH, os.path.basename(dis))

		del_path = False
		if dis_loc:
			try:
				await message.edit(dis_loc)
				del_path = True
				r = requests.post(
					"https://api.deepai.org/api/torch-srgan",
					files={
					    'image': open(dis_loc, 'rb'),
					},
					headers={'api-key': DEEP_API_KEY}
					)
				image_res = r.json()["output_url"]

			except Exception as e_e:
				await message.err(str(e_e))
				return
			try:
				file_, _ = await url_download(message, image_res)
			except Exception as e_e:  # pylint: disable=broad-except
				await message.err(str(e_e))
				return
			string = Path(file_)
			await message.delete()
			await upload_path(message, string, del_path)


@userge.on_cmd("toonify", about={
	'header' : "Coverts any face to toon using AI",
	'description' : "",
	'usage' : ".srgan reply_to_image"
	})
async  def toonify(message: Message):
	if message.reply_to_message:
		await message.edit("Please wait while I toonigy the given media")
		message_ = message.reply_to_message
		if message_.animation:
			await messgage.edit("Animated images are not supported")
			return
		dis = await message.client.download_media(message=message_,file_name=Config.DOWN_PATH)
		dis_loc = os.path.join(Config.DOWN_PATH, os.path.basename(dis))

		del_path = False
		if dis_loc:
			try:
				await message.edit(dis_loc)
				del_path = True
				r = requests.post(
					"https://api.deepai.org/api/toonify",
					files={
					    'image': open(dis_loc, 'rb'),
					},
					headers={'api-key': DEEP_API_KEY}
					)
				image_res = r.json()["output_url"]

			except Exception as e_e:
				await message.err(str(e_e))
				return
			try:
				file_, _ = await url_download(message, image_res)
			except Exception as e_e:  # pylint: disable=broad-except
				await message.err(str(e_e))
				return
			string = Path(file_)
			await message.delete()
			await upload_path(message, string, del_path)

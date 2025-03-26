import sys
import pygame
import importlib as implib

# импорт настроек
import settings as sett

theme = sett.theme
b_sd_x_df = sett.ball_speed_x_default
b_sd_y_df = sett.ball_speed_y_default
rect_sd_y_df = sett.rect_speed_y_default
accelerat = sett.acceleration_game

rect_sz_x = sett.rect_size_x
rect_sz_y = sett.rect_size_y
ball_r = sett.ball_radius
font_sz = sett.font_size

wid = sett.width
hei = sett.height
f_scrn = sett.fullscreen


# импорт конфига темы
th_apply = 'theme.' + theme + '.config'
conf = implib.import_module(th_apply)

bg_menu = conf.background_menu
bg = conf.background
b_img = conf.ball_image
rect_img = conf.rect_image

font_col = conf.font_color
f_set_col = conf.font_select_color

font = conf.font
music = conf.cool_music
sound = conf.cool_sound
nsound = conf.not_cool_sound
################################

def music_load_go(music_path):
	pygame.mixer.music.load(music_path)
	pygame.mixer_music.play(-1)
	return music_path
def sound_load(sound_path):
	sound_path = pygame.mixer.Sound(sound_path)
	return sound_path
def img_tranfr(img_path, x_size, y_size):
	img_path = pygame.image.load(img_path)
	img_path = pygame.transform.scale(img_path, (x_size, y_size))
	return img_path
def fscreen_1_or_0(fullscreen, width, height):
	if fullscreen:
		inf_diply = pygame.display.Info()
		width = inf_diply.current_w
		height = inf_diply.current_h
		screen = pygame.display.set_mode((width, height), pygame.FULLSCREEN, pygame.NOFRAME)
	elif fullscreen == False:
		screen = pygame.display.set_mode((width, height))
	return screen, height, width
def key_rect_up(height, rect_y, rect_speed_y, key):
	keys_inf = pygame.key.get_pressed()
	if keys_inf[key]:
		if rect_y - rect_speed_y > 0:
			rect_y -= rect_speed_y
		else:
			rect_y -= rect_y
	return rect_y
def key_rect_down(height, rect_size_y, rect_y, rect_speed_y, key):
	keys_inf = pygame.key.get_pressed()
	if keys_inf[key]:
		if rect_y + rect_speed_y < height - rect_size_y:
			rect_y += rect_speed_y
		else:
			rect_y += height - (rect_y + rect_sz_y)
	return rect_y
def text_enter(center:bool, x, y, font_color, text, surface, font_size, font_path):
	font = pygame.font.Font(font_path, font_size)
	text = font.render(str(text), True, font_color)
	if center:
		text_xy = text.get_rect(center=(x, y))
	else:
		text_xy = x, y
	return surface.blit(text, text_xy)
def edit_text(text):
	if event.type == pygame.KEYDOWN:
		if event.key == pygame.K_BACKSPACE:
			text = text[:-1]
		else:
			text += event.unicode
	return text
def str_num_edit(string_quantity, string_number):
	if event.type == pygame.KEYDOWN:
		if string_number > 0 and event.key == pygame.K_UP:
			string_number -= 1
		elif string_number < string_quantity - 1 and event.key == pygame.K_DOWN:
			string_number += 1
	return string_number

#########################
pygame.init()
wind_nm = 'PING-PONG'
pygame.display.set_caption(wind_nm)
wid_df = wid
hei_df = hei
scrn, hei, wid = fscreen_1_or_0(f_scrn, wid, hei)
#####################################
wid_div = wid / 2
hei_div = hei / 2
####################################

#################################
#default
menu = 1

score1 = 0
score2 = 0

f_sett_sz = font_sz - 50
active = True
th_input = str(theme)
wid_input = str(wid_df)
hei_input = str(hei_df)
f_scrn_input = str(f_scrn)

b_sd_x_df_input = str(b_sd_x_df)
b_sd_y_df_input = str(b_sd_y_df)
rect_sd_y_df_input = str(rect_sd_y_df)
accelerat_input = str(accelerat)

ball_r_input = str(ball_r)
rect_sz_x_input = str(rect_sz_x)
rect_sz_y_input = str(rect_sz_y)
font_sz_input = str(font_sz)

tutorial_esc_hei = 100

str_num = 0

f_col0 = font_col
f_col1 = font_col
f_col2 = font_col
f_col3 = font_col
f_col4 = font_col

# где находится df
rect1_x_df = 0
rect2_x_df = wid - rect_sz_x
rect_y_df = hei_div - (rect_sz_y/2)
b_x_df = ball_r + rect_sz_x
b_y_df = hei_div - ball_r

#xy = xy_df
rect1_x = rect1_x_df
rect1_y = rect_y_df
rect2_x = rect2_x_df
rect2_y = rect_y_df
ball_x = b_x_df
ball_y = b_y_df
##################################


#############################
ball_sd_x = b_sd_x_df
ball_sd_y = b_sd_y_df
rect_sd_y = rect_sd_y_df
################################
ball_d = ball_r * 2
############################


################################
#music
music = music_load_go(music)
sound = sound_load(sound)
nsound = sound_load(nsound)
#################################


#####################################
bg = img_tranfr(bg, wid, hei)
bg_menu = img_tranfr(bg_menu, wid, hei)
b_img = img_tranfr(b_img, ball_d, ball_d)
rect_img = img_tranfr(rect_img, rect_sz_x, rect_sz_y)
###################################################################


###############################################################################
while True:
####################################################
	keys = pygame.key.get_pressed()
######################################################

	for event in pygame.event.get():
		#выход по ESC
		if event.type == pygame.QUIT:
			pygame.quit()
			sys.exit()
#################################################################
		if menu == 1:
			str_num = str_num_edit(3, str_num)
			if str_num == 0:
				f_col0 = f_set_col
				if event.type == pygame.KEYDOWN:
					if event.key == pygame.K_RETURN:
						str_num = 0
						menu = 0
						score1 = 0
						score2 = 0
						tutorial_esc_hei = 0

						rect1_x = rect1_x_df
						rect1_y = rect_y_df
						rect2_x = rect2_x_df
						rect2_y = rect_y_df
						ball_x = b_x_df
						ball_y = b_y_df

						ball_sd_x = b_sd_x_df
						ball_sd_y = b_sd_y_df
						rect_sd_y = rect_sd_y_df
			else: f_col0 = font_col

			if str_num == 1:
				f_col1 = f_set_col
				if event.type == pygame.KEYDOWN:
					if event.key == pygame.K_RETURN:
						str_num = 0
						menu = 2
			else:
				f_col1 = font_col

			if str_num == 2:
				f_col2 = f_set_col
				if event.type == pygame.KEYDOWN:
					if event.key == pygame.K_RETURN:
						pygame.quit()
						sys.exit()
			else:
				f_col2 = font_col

		##############################################################
		elif menu == 2:
			str_num = str_num_edit(4, str_num)
			if str_num == 0:
				f_col0 = f_set_col
				if event.type == pygame.KEYDOWN:
					if event.key == pygame.K_RETURN:
						str_num = 0
						menu = 'th&scrn'
			else: f_col0 = font_col

			if str_num == 1:
				f_col1 = f_set_col
				if event.type == pygame.KEYDOWN:
					if event.key == pygame.K_RETURN:
						str_num = 0
						menu = 'speed'
			else: f_col1 = font_col

			if str_num == 2:
				f_col2 = f_set_col
				if event.type == pygame.KEYDOWN:
					if event.key == pygame.K_RETURN:
						str_num = 0
						menu = 'size'
			else: f_col2 = font_col
			
			if str_num == 3:
				f_col3 = f_set_col
				if event.type == pygame.KEYDOWN:
					if event.key == pygame.K_RETURN:
						str_num = 0
						menu = 1

			else: f_col3 = font_col
#######################################################3
		elif menu == 'th&scrn':
			str_num = str_num_edit(5, str_num)
			if str_num == 0:
				f_col0 = f_set_col
				th_input = edit_text(th_input)
			else: f_col0 = font_col

			if str_num == 1:
				f_col1 = f_set_col
				wid_input = edit_text(wid_input)
			else: f_col1 = font_col

			if str_num == 2:
				f_col2 = f_set_col
				hei_input = edit_text(hei_input)
			else: f_col2 = font_col

			if str_num == 3:
				f_col3 = f_set_col
				f_scrn_input = edit_text(f_scrn_input)
			else: f_col3 = font_col

			if str_num == 4:
				if event.type == pygame.KEYDOWN:
					if event.key == pygame.K_RETURN:
						str_num = 0
						menu = 2
				f_col4 = f_set_col
			else: f_col4 = font_col
###############################################################3		
		elif menu == 'speed':
			str_num = str_num_edit(5, str_num)
			if str_num == 0:
				f_col0 = f_set_col
				b_sd_x_df_input = edit_text(b_sd_x_df_input)
			else: f_col0 = font_col

			if str_num == 1:
				f_col1 = f_set_col
				b_sd_y_df_input = edit_text(b_sd_y_df_input)
			else: f_col1 = font_col

			if str_num == 2:
				f_col2 = f_set_col
				rect_sd_y_df_input = edit_text(rect_sd_y_df_input)
			else: f_col2 = font_col

			if str_num == 3:
				f_col3 = f_set_col
				accelerat_input = edit_text(accelerat_input)
			else: f_col3 = font_col

			if str_num == 4:
				if event.type == pygame.KEYDOWN:
					if event.key == pygame.K_RETURN:
						str_num = 1
						menu = 2
				f_col4 = f_set_col
			else: f_col4 = font_col
		
		elif menu == 'size':
			str_num = str_num_edit(5, str_num)
			if str_num == 0:
				f_col0 = f_set_col
				ball_r_input = edit_text(ball_r_input)
			else: f_col0 = font_col

			if str_num == 1:
				f_col1 = f_set_col
				rect_sz_x_input = edit_text(rect_sz_x_input)
			else: f_col1 = font_col

			if str_num == 2:
				f_col2 = f_set_col
				rect_sz_y_input = edit_text(rect_sz_y_input)
			else: f_col2 = font_col

			if str_num == 3:
				f_col3 = f_set_col
				font_sz_input = edit_text(font_sz_input)
			else: f_col3 = font_col

			if str_num == 4:
				if event.type == pygame.KEYDOWN:
					if event.key == pygame.K_RETURN:
						str_num = 2
						menu = 2
				f_col4 = f_set_col
			else: f_col4 = font_col


###########################################################


############################################################

	if menu == 2:
		scrn.blit(bg_menu, (0, 0))
		text_enter(False, 100, hei_div-(font_sz*2), f_col0, 'THEME & SCREEN', scrn, font_sz, font)
		text_enter(False, 100, hei_div-font_sz, f_col1, 'SPEED', scrn, font_sz, font)
		text_enter(False, 100, hei_div, f_col2, 'SIZE', scrn, font_sz, font)
		text_enter(False, 100, hei_div+(font_sz*2), f_col3, 'BACK', scrn, font_sz, font)

#######################################################################################3
	elif menu == 'th&scrn':
		scrn.blit(bg_menu, (0, 0))
		text_enter(False, 100, 100, f_col0, f'theme: {th_input}', scrn, f_sett_sz, font)
		text_enter(False, 100, 250, f_col1, f'width: {wid_input}', scrn, f_sett_sz, font)
		text_enter(False, 100, 350, f_col2, f'height: {hei_input}', scrn, f_sett_sz, font)
		text_enter(False, 100, 450, f_col3, f'fullscreen: {f_scrn_input}', scrn, f_sett_sz, font)
		text_enter(False, 100, 600, f_col4, 'BACK', scrn, f_sett_sz, font)
##############################################
	elif menu == 'speed':
		scrn.blit(bg_menu, (0, 0))
		text_enter(False, 100, 150, f_col0, f'ball speed x default: {b_sd_x_df_input}', scrn, f_sett_sz, font)
		text_enter(False, 100, 250, f_col1, f'ball speed y default: {b_sd_y_df_input}', scrn, f_sett_sz, font)
		text_enter(False, 100, 350, f_col2, f'rect speed y default: {rect_sd_y_df_input}', scrn, f_sett_sz, font)
		text_enter(False, 100, 500, f_col3, f'acceleration: {accelerat_input}', scrn, f_sett_sz, font)
		text_enter(False, 100, 650, f_col4, 'BACK', scrn, f_sett_sz, font)
	
	elif menu == 'size':
		scrn.blit(bg_menu, (0, 0))
		text_enter(False, 100, 150, f_col0, f'ball radius: {ball_r_input}', scrn, f_sett_sz, font)
		text_enter(False, 100, 250, f_col1, f'rect size x: {rect_sz_x_input}', scrn, f_sett_sz, font)
		text_enter(False, 100, 350, f_col2, f'rect size y: {rect_sz_y_input}', scrn, f_sett_sz, font)
		text_enter(False, 100, 500, f_col3, f'font size: {font_sz_input}', scrn, f_sett_sz, font)
		text_enter(False, 100, 650, f_col4, 'BACK', scrn, f_sett_sz, font)
##########################################################
	elif menu == 1:
		scrn.blit(bg_menu, (0, 0))

		# текст в главном меню
		text_enter(True, wid_div, hei_div-(font_sz*2), font_col, 'PING-PONG', scrn, font_sz, font)
		text_enter(True, wid_div, hei_div-font_sz, f_col0, 'PLAY', scrn, font_sz, font)
		text_enter(True, wid_div, hei_div, f_col1, 'SETTINGS', scrn, font_sz, font)
		text_enter(True, wid_div, hei_div+font_sz*2, f_col2, 'EXIT', scrn, font_sz, font)
##################################################


#################################################################
	elif menu == 0:
		tutorial_esc_hei +=10
		if keys[pygame.K_ESCAPE]:
			menu = 1
		scrn.blit(bg, (0,0))
		scrn.blit(b_img, (ball_x, ball_y))
		scrn.blit(rect_img, (rect1_x, rect1_y))
		scrn.blit(rect_img, (rect2_x, rect2_y))
###############################################################
		text_enter(True, wid_div, tutorial_esc_hei, font_col, 'ESC >> MENU', scrn, f_sett_sz, font)
		text_enter(True, 500, 100, font_col, score1, scrn, font_sz, font)
		text_enter(True, wid - 500, 100, font_col, score2, scrn, font_sz, font)
		text_enter(True, wid_div, 100, font_col, '|', scrn, font_sz, font)
###############################################################
		# движение плитками
		rect1_y = key_rect_up(hei, rect1_y, rect_sd_y, pygame.K_w)
		rect2_y = key_rect_up(hei, rect2_y, rect_sd_y, pygame.K_UP)
		rect1_y = key_rect_down(hei, rect_sz_y, rect1_y, rect_sd_y, pygame.K_s)
		rect2_y = key_rect_down(hei, rect_sz_y, rect2_y, rect_sd_y, pygame.K_DOWN)
###########################################################

		# столкновение мяча с плитками
		rect1_rect = pygame.Rect(rect1_x, rect1_y, rect_sz_x, rect_sz_y)
		rect2_rect = pygame.Rect(rect2_x, rect2_y, rect_sz_x, rect_sz_y)
		ball_rect = pygame.Rect(ball_x, ball_y, ball_d, ball_d)

		if rect1_rect.colliderect(ball_rect):
			sound.play()
			ball_sd_x = -ball_sd_x

			if ball_x <= rect_sz_x:
				ball_x = rect_sz_x + 5

			ball_sd_x += accelerat
			ball_sd_y += accelerat
			rect_sd_y += accelerat

		if rect2_rect.colliderect(ball_rect):
			sound.play()
			ball_sd_x = -ball_sd_x

			if ball_x + ball_d >= wid - rect_sz_x:
				ball_x = wid - (ball_d + rect_sz_x + 5)

			ball_sd_x += -accelerat
			ball_sd_y += -accelerat
			rect_sd_y += accelerat
######################################################

		# движение мяча
		ball_x += ball_sd_x
		ball_y += ball_sd_y

		if ball_x <=0:
			nsound.play()
			score2 += 1
			ball_x = wid_div - ball_r
			ball_y = hei_div - ball_r
			ball_sd_y = -ball_sd_y
			scrn.blit(bg, (0, 0))
			scrn.blit(b_img, (ball_x, ball_y))
			pygame.time.Clock().tick(120)
			pygame.display.flip()
			pygame.time.wait(1000)
		if ball_x + ball_d >= wid:
			nsound.play()
			score1 += 1
			ball_x = wid_div - ball_r
			ball_y = hei_div - ball_r
			ball_sd_y = -ball_sd_y
			scrn.blit(bg, (0, 0))
			scrn.blit(b_img, (ball_x, ball_y))
			pygame.time.Clock().tick(120)
			pygame.display.flip()
			pygame.time.wait(1000)
		if ball_y + ball_d >= hei or ball_y <= 0:
			ball_sd_y = -ball_sd_y
####################################################################
	# Ограничение частоты кадров и обновление экрана
	pygame.time.Clock().tick(120)
	pygame.display.flip()


	file_sett = open('ping_pong_by_zkp/settings.py', 'w')
	file_sett.close()
	file_sett = open('ping_pong_by_zkp/settings.py', 'w')
	file_sett.write(
		f'theme = \'{th_input}\' \n'
		f'width = {wid_input} \n'
		f'height = {hei_input} \n'
		f'fullscreen = {f_scrn_input} \n\n'

		f'ball_speed_x_default = {b_sd_x_df_input} \n'
		f'ball_speed_y_default = {b_sd_y_df_input} \n'
		f'rect_speed_y_default = {rect_sd_y_df_input} \n'
		f'acceleration_game = {accelerat_input} \n\n'

		f'rect_size_x = {rect_sz_x_input} \n'
		f'rect_size_y = {rect_sz_y_input} \n'
		f'ball_radius = {ball_r_input} \n'
		f'font_size = {font_sz_input} \n'
		)

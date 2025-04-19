import os
main_dir = os.path.dirname(__file__)
file_sett_path = main_dir + '/settings.py'
file_sett = open(file_sett_path, 'w')
file_sett.close()
file_sett = open(file_sett_path, 'w')
file_sett.write(
    'theme = \'default\' \n'
    'width = 1500 \n'
    'height = 1000 \n'
    'fullscreen = 1 \n\n'

    'ball_speed_x_default = 20 \n'
    'ball_speed_y_default = 20 \n'
    'rect_speed_y_default = 10 \n'
    'acceleration_game = 0.1 \n\n'

    'rect_size_x = 50 \n'
    'rect_size_y = 150 \n'
    'ball_radius = 30 \n'
    'font_size = 80 \n'
)

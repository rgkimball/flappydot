# rgkimball | rgk.io
# 2016/12/11

h = 800
w = 600
bg = "#000"
birdcolor = "#f00"
framerate = 110  # frames per second; modifies the sleep function

gravity = 0.35  # pixels added to bird velocity per frame
bird_lift = 55  # multiplied by gravity to determine how fast the bird jumps
maxvelocity = 10  # maximum absolute velocity
fall_multiplier = 1.5  # max fall speed, as a multiple of maxvelocity
bird_size = 0.075  # calculated as a percentage of window height

pipe_gap = 0.33 * h
pipe_width = 0.12 * w
pipe_color = "#ccc"
pipe_speed = 2  # pixels per frame
pipe_frequency = 160  # measured in frames per pipe

death_forgiveness = 7  # allowance for hitting pipes; in pixels

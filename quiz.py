import pgzrun

WIDTH = 1280
HEIGHT = 720


main_box = Rect(0, 0, 820, 240)

timer_box = Rect(0, 0, 240, 240)

answer_box1 = Rect(0, 0, 495, 165)
answer_box2 = Rect(0, 0, 495, 165)
answer_box3 = Rect(0, 0, 495, 165)
answer_box4 = Rect(0, 0, 495, 165)

main_box.move_ip(50, 40)

timer_box.move_ip(990, 40)

answer_box1.move_ip(50, 358)

answer_box2.move_ip(735, 358)

answer_box3.move_ip(50, 538)

answer_box4.move_ip(735, 538)

answer_boxes = [answer_box1, answer_box2, answer_box3, answer_box4]


score = 0

time_left = 30

q1 = ["How do you terminated an statement in JS", ":", ";", "#", "}", 2]

q2 = ["How do you define a Function in JS", "func", "myFunction", "console", "function", 4]

q3 = ["How do you define an Array", "{}", "[a, b]", "();", "{a, b}", 2]

q4 = ["What DOM means", "Demographic or Methodology", "Document of Menace", "Document Object Model", "Display of Model", 3]

q5 = ["What is an event Listener", "button", "action", "Method", "Array", 3]


questions = [q1, q2, q3, q4, q5]

question = questions.pop(0)

def draw():
    screen.fill("dim gray")
    screen.draw.filled_rect(main_box, "sky blue")
    screen.draw.filled_rect(timer_box, "sky blue")

    for box in answer_boxes:
        screen.draw.filled_rect(box, "orange")
        
    
    screen.draw.textbox(str(time_left), timer_box, color=("black"))
    screen.draw.textbox(question[0], main_box, color=("black"))
    index = 1
    for box in answer_boxes:
        screen.draw.textbox(question[index], box, color=("black"))
        index = index + 1

def game_over():
    pass

def correct_answer():
    pass

def on_mouse_down(pos):
    pass

def Update_time_left():
    pass







pgzrun.go()






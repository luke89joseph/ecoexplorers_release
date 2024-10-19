  ### app

app.background = 'green'
app.status = 'intro'
app.stepsPerSecond = 30
app.message = False
app.messageTimer = 90
app.devHack = False

menuTrack = Sound('https://raw.githubusercontent.com/luke89joseph/ecoexplorers/main/retroTrack.mp3')
solarMusic = Sound('https://raw.githubusercontent.com/luke89joseph/ecoexplorers/main/solarChallenge.mp3')
geoThermalMusic = Sound('https://raw.githubusercontent.com/luke89joseph/ecoexplorers/main/geothermalChallenge2.mp3')
windMusic = Sound('https://raw.githubusercontent.com/luke89joseph/ecoexplorers/main/windChallenge.mp3')
ozoneMusic = Sound('https://raw.githubusercontent.com/luke89joseph/ecoexplorers/main/ozoneChallenge.mp3')
ecoMusic = Sound('https://raw.githubusercontent.com/luke89joseph/ecoexplorers/main/ecosystemChallenge.mp3')
finalTrack = Sound('https://raw.githubusercontent.com/luke89joseph/ecoexplorers/main/FinalTrack.mp3')

app.geoTherm = False
app.geoChallenge = False
app.geoScore = 0
app.geoStage = 0
app.geoDrag = 0

app.solarPower = False
app.solarChallenge = False
app.solarScore = 0
app.solarThrust = 0
app.solarFact = 1
app.solarBattery = 7
app.solarDrag = 0

app.windPower = False
app.windChallenge = False
app.windScore = 0
app.windFact = 0
app.windGravity = True
app.windThrust = True
app.windThrustTimer = 60
app.windDrag = 0

app.ozoneLayer = False
app.ozoneChallenge = False
app.ozoneFact = 0
app.ozoneScore = 0
app.ozoneDrag = 0
app.ozoneInvaderDirection = 1

app.ecosystem = False
app.ecosystemChallenge = False
app.ecosystemScore = 0
app.ecosystemDrag = 0
app.ecoFlyTimer = 200
app.ecoTongueTimer = -10
app.ecoFlyCount = 0
app.ecoFliesPast = 0

app.trophy = False
app.trophyChallenge = False
app.trophyStatus = 1

app.password = ''
app.keywords = []
app.currentKeyword = ''
app.letters = ['a', 'b', 'c', 'j4', 'e', 'f', 'g', 'i9', 'i8', 'j5', '3d8']

import random

app.tagline = 0

loadingScreen = Group (
    Rect (0, -600, 400, 500, fill='grey'),
    Label ('| EcoExplorers |', 200, -500, fill='white', font='montserrat', bold=True, size=40),
    )
loadingSquare = Rect (0, -100, 400, 500, fill='darkGreen', visible = False)
loadingTrees = Group ()
def loading():
    i = 0
    loadingSquare.visible = True
    loadingTrees.add(loadingScreen, loadingSquare)
    for i in range(500):
        newTree = Group (
            Polygon (300, 33, 275, 75, 325, 75, fill=rgb (0, random.randint(50, 100), 0)),
            Rect (290, 75, 20, 25, fill='saddleBrown'),
            )
        newTree.centerX = random.randint(0, 400)
        newTree.centerY = random.randint(-400, 0)
        loadingTrees.add(newTree)
        i += 1

### Shapes

introScreen = Group (
    Rect (0, 0, 400, 400, fill=None, border='darkGreen', borderWidth = 10),
    Label ('EcoExplorers |', 150, 70, fill='white', bold=True, font='montserrat', size=30),
    Polygon (300, 33, 275, 75, 325, 75, fill='darkGreen'),
    Rect (290, 75, 20, 25, fill='saddleBrown'),
    Line (35, 111, 365, 111, fill='lightGreen', dashes=True, lineWidth=5),
    Label ('v1.1', 370, 380, fill='white', bold=True)
    )
introTagline = Label ('', 200, 130, fill='lightGreen', size=13, bold=True, font='montserrat')
app.tagline = random.randint(1,11)
if (app.tagline == 1):
    introTagline.value = '| Level up your eco-awareness |'
elif (app.tagline == 2):
    introTagline.value = '| Play to learn, learn to change the world |'
elif (app.tagline == 3):
    introTagline.value = '| Reimagine the future |'
elif (app.tagline == 4):
    introTagline.value = '| Go hug a tree when you are done |'
elif (app.tagline == 5):
    introTagline.value = '| Planting seeds of knowledge |'
elif (app.tagline == 6):
    introTagline.value = '| Reimagine the future |'
elif (app.tagline == 7):
    introTagline.value = '| Open source on Github |'
elif (app.tagline == 8):
    introTagline.value = '| To tree or not to tree, that is the question |'
elif (app.tagline == 9):
    introTagline.value = '| Climate change bad  |'
elif (app.tagline == 10):
    introTagline.value = '| ecoexplorers.gitbook.io :D |'
elif (app.tagline == 11):
    introTagline.value = '| Go touch grass when you are done |'
    
introScreen.add(introTagline)

goButton = Group (
    Rect (100, 190, 200, 70, fill='lightGreen', border='darkGreen', borderWidth=5),
    )
goLabel = Label ('Create Account', 200, 225, fill='darkGreen', size=18, font='montserrat', bold=True)
goButton.add (goLabel)

loginButton = Group (
    Rect (100, 290, 200, 70, fill='lightGreen', border='darkGreen', borderWidth=5)
    )
loginLabel = Label ('Login', 200, 325, font='montserrat', size=18, bold=True, fill='darkGreen')
loginButton.add(loginLabel)

introScreen.add (
    goButton,
    loginButton,
    )
app.name = 0

certifyLabel = Label(app.name, 200, 150, font='montserrat', bold=True, size=20)

certify = Group (
    Rect(50, 100, 300, 200, fill='lightGrey', border='grey', borderWidth = 5),
    Label("This certifies that...", 200, 120, font='grenze'),
    Label("has completed", 200, 185, font='grenze'),
    Label("EcoExplorers", 200, 200, size = 20, bold=True, font='grenze'),
    Star(200, 250, 30, 8, fill='yellow', border='gold', borderWidth = 3),
    Label("Congratulations! You've completed EcoExplorers!", 200, 350, font='montserrat', bold=True),
    Label("Screenshot this certificate and click anywhere to return home", 200, 380, font='montserrat'),
    )
certify.add(certifyLabel)
certify.visible = False  

trophy1 = Star(25, 35, 20, 5, fill='gold')
trophy2 = Star(305, 68, 20, 5, fill='gold')
trophy3 = Star(111, 43, 30, 5, fill='yellow', border='gold')
trophy4 = Star(362, 23, 30, 5, fill='yellow', border='gold')
trophy5 = Star(220, 35, 35, 8, fill='darkKhaki')

winEffect = Group (
    trophy1,
    trophy2,
    trophy3,
    trophy4,
    trophy5
    )
winEffect.visible = False

### Testing Settings
introScreen.visible = True
app.status = 'intro'

#loadingScreen.visible = False
#introScreen.visible = False
###

menuTitle = Label ('| BADGES |', 200, 40, size=30, fill='white', bold=True, font='montserrat')

menu = Group (
    Line (55, 67, 355, 67, fill='white', dashes=True, lineWidth=5),
    Label ('EARN THEM ALL', 200, 88, fill='white', font='montserrat', bold=True),
    )
    
saveButton = Group (
    Rect (335, 0, 65, 40, fill=None),
    Label ('SAVE', 365, 25, fill='white', bold=True, font='montserrat'),
    )
    
menu.add(saveButton)

### Testing Settings
#menu.visible = True
###
    
geoThermBadgePart = Circle (75, 150, 45, fill='grey', borderWidth=5, border='black')
geoThermPart2 = Oval (75, 150, 40, 65, fill='silver')
geoThermPart3 = Oval (75, 158, 20, 45, fill='gainsboro')
geoThermPart4 = Line (39, 131, 111, 174, lineWidth=5)
geoThermLabel = Label ('GEOTHERMAL', 75, 210, fill='darkGrey', font='montserrat', bold=True, size=12)
geoThermBadge = Group (
    geoThermBadgePart,
    geoThermPart2,
    geoThermPart3,
    geoThermPart4,
    geoThermLabel
    )
    
solarPowerBadgePart = Circle (200, 150, 45, fill='grey', borderWidth=5, border='black')
solarPowerPart2 = Star (200, 150, 30, 9, fill='silver')
solarPowerPart3 = Circle (200, 150, 20, fill='gainsboro')
solarPowerPart4 = Line (160, 131, 233, 174, lineWidth=5)
solarPowerLabel = Label ('SOLAR', 200, 210, fill='darkGrey', font='montserrat', bold=True, size=12)

solarPowerBadge = Group (
    solarPowerBadgePart,
    solarPowerPart2,
    solarPowerPart3,
    solarPowerPart4,
    solarPowerLabel
    )
    
windPowerBadgePart = Circle (325, 150, 45, fill='grey', borderWidth=5, border='black')
windPowerPart2 = Line (325, 190, 325, 150, lineWidth = 10, fill='silver')
windPowerPart3 = Star (325, 150, 30, 3, fill='gainsboro', roundness=20, rotateAngle=20)
windPowerPart4 = Line (285, 131, 360, 174, lineWidth=5)
windPowerLabel = Label ('WIND', 325, 210, fill='darkGrey', font='montserrat', bold=True, size=12)

windPowerBadge = Group (
    windPowerBadgePart,
    windPowerPart2,
    windPowerPart3,
    windPowerPart4,
    windPowerLabel
    )
    
ozoneBadgePart = Circle (75, 290, 45, fill='grey', borderWidth=5, border='black')
ozonePart2 = Circle (75, 290, 30, fill='darkBlue')
ozonePart2.fill = rgb(62, 60, 60)
ozonePart3 = Group (
    Oval (65, 280, 20, 10, fill='green'),
    Oval (75, 285, 20, 10, fill='green'),
    Oval (65, 288, 15, 20, fill='green'),
    Oval (70, 305, 20, 10, fill='green', rotateAngle = 65),
    Oval (88, 296, 20, 10, fill='green', rotateAngle = 350),
    Oval (90, 302, 20, 10, fill='green', rotateAngle = 115),
    )
ozonePart3.fill = 'gainsboro'
ozonePart4 = Line (39, 271, 111, 314, lineWidth=5)
ozoneLabel = Label ('OZONE', 75, 350, fill='darkGrey', font='montserrat', bold=True, size=12)
ozoneBadge = Group (
    ozoneBadgePart,
    ozonePart2,
    ozonePart3,
    ozonePart4,
    ozoneLabel
    )


ecosystemBadgePart = Circle (200, 290, 45, fill='grey', borderWidth=5, border='black')
ecosystemPart2 = Group (
    Oval (200, 300, 60, 50, fill='silver'),
    Oval (175, 280, 20, 20, fill='silver'),
    Oval (225, 280, 20, 20, fill='silver'),
    Circle (175, 280, 6, fill='dimGrey'),
    Circle (225, 280, 6, fill='dimGrey'),
    Circle (175, 280, 4, fill='dimGrey'),
    Circle (225, 280, 4, fill='dimGrey'),
    )

ecosystemPart3 = Arc (200, 305, 20, 20, 90, 180, fill='dimGrey')
ecosystemPart4 = Line (160, 271, 233, 314, lineWidth=5)
ecosystemLabel = Label ('ECOSYSTEM', 200, 350, fill='darkGrey', font='montserrat', bold=True, size=12)
ecosystemBadge = Group (
    ecosystemBadgePart,
    ecosystemPart2,
    ecosystemPart3,
    ecosystemPart4,
    ecosystemLabel
    )
    
trophyBadgePart = Circle (328, 290, 45, fill='grey', borderWidth=5, border='black')
trophyLabel = Label ('{[-LOCKED-]}', 328, 350, fill='darkGrey', font='montserrat', bold=True, size=12)
trophyBadgePart3 = Oval(328, 280, 50, 20, fill=None, borderWidth = 4, border = 'darkGrey')
trophyBadgePart2 = Polygon(315, 270, 345, 270, 345, 295, 338, 300, 340, 320, 320, 320, 322, 300, 315, 295, fill='darkGrey')
trophyBadgePart4 = Star(338, 268, 10, 4, fill='darkKhaki', opacity = 0)
trophyBadgePart2.centerX = trophyBadgePart.centerX
trophyBadgePart2.centerY = trophyBadgePart.centerY
trophyBadge = Group (
    trophyBadgePart,
    trophyLabel,
    trophyBadgePart3,
    trophyBadgePart2,
    trophyBadgePart4
    )
    
menu.add (
    geoThermBadge,
    menuTitle,
    solarPowerBadge,
    windPowerBadge,
    ozoneBadge,
    ecosystemBadge,
    trophyBadge,
    )
menu.visible = False

messageBox = Rect (0, 0, 400, 80, fill='white', border='gainsboro', borderWidth = 5)
messageLabel = Label ('', 200, 28, fill='grey', size=15, font='montserrat')
messageLabel2 = Label ('', 200, 58, fill='grey', size=15, font='montserrat')
message = Group (
    messageBox,
    messageLabel,
    messageLabel2,
    )
message.centerY = -50
message.visible = False

passwordBox = Group (
    Rect (0, 330, 400, 70, fill='white', border='gainsboro'),
    Label ('| WRITE DOWN PASSWORD, TAP BOX TO HIDE |', 200, 380, fill='grey', size=15, font='montserrat')
    )
passwordLabel = Label ('', 200, 350, fill='grey', font='montserrat')
passwordBox.add (passwordLabel)
passwordBox.visible = False

### Geothermal Challenge Shapes

geoThermStart = Group(
    Rect (0, 100, 400, 50, fill='green'),
    Rect (0, 0, 400, 100, fill='skyBlue'),
    Rect (0, 150, 400, 30, fill='saddleBrown'),
    Rect (165, 50, 70, 50, fill='darkRed'),
    Polygon (200, 10, 150, 50, 250, 50, fill='grey'),
    Rect (190, 70, 20, 30, fill='goldenRod'),
    )
geoThermStart.visible = False

geoPipe = Line (200, 160, 200, 200, fill='darkGrey', lineWidth=20)
geoPipe.visible = False
geoPipe2 = Rect (180, 195, 35, 20, fill='silver')
geoPipe2.centerX = 200
geoPipe2.visible = False
geoThermStart.toFront()

geoThermCourse1 = Group (
    Rect (202, 150, 200, 50, fill='dimGrey'),
    Rect (0, 265, 200, 50, fill='dimGrey'),
    )
geoThermCourse1.visible = False
geoFact1 = Group (
    Label ('Geothermal power is', 306, 220, fill='white', font='montserrat', size=15),
    Label ('a renewable form of energy', 280, 240, fill='white', font='montserrat', size=15),
    )
geoFact1.visible = False

geoThermCourse2 = Group  (
    Rect (-200, 150, 400, 50, fill='dimGrey'),
    Rect (300, 265, 450, 50, fill='dimGrey'),
    )
geoThermCourse2.visible = False
geoThermCourse2.movement = 'left'
geoFact2 = Group (
    Label ('Geothermal powerplants are able to', 145, 347, fill='white', font='montserrat', size=15),
    Label ('produce energy consistantly, 24/7', 145, 372, fill='white', font='montserrat', size=15)
    )
geoFact2.visible = False

geoThermCourse3 = Group (
    Rect (282, 100, 100, 70, fill='dimGrey'),
    Rect (390, 300, 100, 70, fill='dimGrey'),
    Rect (28, 190, 70, 100, fill='dimGrey'),
    Rect (138, 336, 200, 50, fill='dimGrey'),
    )
geoThermCourse3.visible = False
geoFact3 = Group (
    Label ('Geothermal power is energy', 270, 220, fill='white', font='montserrat', size=15),
    Label ('derived from the heat from', 280, 240, fill='white', font='montserrat', size=15),
    Label ('the core of the Earth', 306, 260, fill='white', font='montserrat', size=15),
    )
geoFact3.visible = False

geoThermCourse4 = Group (
    Line (111, 100, 367, 100, fill='dimGrey', lineWidth = 30),
    Line (335, 200, 300, 341, fill='dimGrey', lineWidth = 30),
    Line (218, 290, 100, 290, fill='dimGrey', lineWidth = 30),
    Line (100, 160, 100, 90, fill='dimGrey', lineWidth = 30),
    )
geoThermCourse4.visible = False
geoThermCourse4.centerX = 200
geoThermCourse4.centerY += 50
geoFact4 = Group (
    Label ('The steam generated by', 295, 30, fill='white', font='montserrat', size=15),
    Label ('geothermal plants drive', 295, 50, fill='white', font='montserrat', size=15),
    Label ('turbines which generate electricity', 265, 70, fill='white', font='montserrat', size=15),
    )
geoFact4.visible = False

geoThermCourse5 = Group (
    Line (111, 130, 367, 130, fill='dimGrey', lineWidth = 30),
    Line (320, 290, 0, 290, fill='dimGrey', lineWidth = 30),
    Line (100, 200, 111, 130, fill='dimGrey', lineWidth = 30),
    Line (100, 360, 380, 360, fill='dimGrey', lineWidth = 30),
    )
geoThermCourse5.visible = False
geoThermCourse5p2 = Group (
    Line (335, 200, 300, 340, fill='dimGrey', lineWidth = 30),
    Line (100, 200, 100, 290, fill='dimGrey', lineWidth = 30),
    )
geoThermCourse5p2.visible = False
geoThermCourse5p2.movement = 'Up'
geoFact5 = Group (
    Label ('One of the most active geothermal', 265, 30, fill='white', font='montserrat', size=15),
    Label ('areas in the world is the Ring of', 265, 50, fill='white', font='montserrat', size=15),
    Label ('Fire, which encircles the Pacific', 265, 70, fill='white', font='montserrat', size=15),
    )
geoFact5.visible = False

geoThermQuestions = Group ()
geoQuestion1 = Label ('Geothermal energy is a _______ form of energy', 200, 120, size=13, font='montserrat', fill='white', bold=True)
geoQuestion2 = Label ('Geothermal powerplants _______ produce energy', 200, 160, size=13, font='montserrat', fill='white', bold=True)
geoQuestion3 = Label ('Geothermal power is derived from ______', 200, 200, size=13, font='montserrat', fill='white', bold=True)
geoQuestion4 = Label ('The steam drives _______ which generate electricity', 200, 240, size=13, font='montserrat', fill='white', bold=True)
geoQuestion5 = Label ('The _______ is one of the most active geothermal parts of the world', 200, 280, size=11, font='montserrat', fill='white', bold=True)
geoThermQuestions.add (
    geoQuestion1,
    geoQuestion2,
    geoQuestion3,
    geoQuestion4,
    geoQuestion5
    )
geoThermQuestions.visible = False

geoThermAnswers = Group()
geoAnswer1 = Label ('RENEWABLE', 80, 360, size=15, font='montserrat', fill='white', bold=True)
geoAnswer2 = Label ('CONSISTANTLY', 300, 360, size=15, font='montserrat', fill='white', bold=True)
geoAnswer3 = Label ('HEAT', 190, 360, size=15, font='montserrat', fill='white', bold=True)
geoAnswer4 = Label ('TURBINES', 140, 320, size=15, font='montserrat', fill='white', bold=True)
geoAnswer5 = Label ('RING OF FIRE', 250, 320, size=15, font='montserrat', fill='white', bold=True)
geoThermAnswers.add (
    geoAnswer1,
    geoAnswer2,
    geoAnswer3,
    geoAnswer4,
    geoAnswer5,
    )
geoThermAnswers.visible = False


### Solar Power Challenge Shapes

solarCar = Group(
    Oval (188, 213, 15, 10),
    Oval (210, 213, 15, 10),
    Oval (188, 188, 15, 10),
    Oval (210, 188, 15, 10),
    Oval (200, 200, 60, 25, fill='gainsboro'),
    Rect (168, 190, 10, 20, fill='silver'),
    Polygon (182, 194, 182, 205, 197, 208, 197, 190, fill='dimGrey'),
    Polygon (210, 190, 210, 210, 222, 207, 222, 192, fill='midnightBlue')
    )
solarCar.visible = False
solarCar.centerX = 40


solarTrack1 = Line (0, 200, 420, 200, fill='grey', lineWidth=200, visible = False)
solarLine1 = Line (0, 200, 800, 200, fill='yellow', lineWidth = 5, dashes = True, visible = False)

solarOrb  = Group (
    Circle (200, 200, 10, fill='gold', opacity = 50),
    Circle (200, 200, 5, fill='yellow')
    )
solarOrb.visible = False

solarCourse1 = Group (
    Rect (556, 128, 40, 40, fill='darkGrey'),
    Rect (650, 220, 40, 40, fill='darkGrey'),
    Rect (850, 200, 40, 40, fill='darkGrey'),
    Rect (1200, 100, 40, 40, fill='darkGrey'),
    Rect (1200, 250, 40, 40, fill='darkGrey'),
    Rect (1200, 150, 40, 40, fill='darkGrey'),
    Rect (1500, 250, 40, 40, fill='darkGrey'),
    Rect (1550, 200, 40, 40, fill='darkGrey'),
    Rect (1700, 150, 40, 40, fill='darkGrey'),
    Rect (1700, 105, 40, 40, fill='darkGrey'),
    )
solarCourse1.rotateAngle = 0

solarCourse2 = Group (
    Rect (556, 105, 40, 40, fill='darkGrey'),
    Rect (556, 155, 40, 40, fill='darkGrey'),
    Rect (750, 205, 40, 40, fill='darkGrey'),
    Rect (750, 255, 40, 40, fill='darkGrey'),
    Rect (950, 105, 40, 40, fill='darkGrey'),
    Rect (950, 155, 40, 40, fill='darkGrey'),
    Rect (1150, 205, 40, 40, fill='darkGrey'),
    Rect (1150, 255, 40, 40, fill='darkGrey'),
    Rect (1550, 170, 40, 40, fill='darkGrey'),
    Rect (1550, 105, 40, 40, fill='darkGrey'),
    Rect (1400, 255, 40, 40, fill='darkGrey'),
    Rect (1800, 105, 40, 40, fill='darkGrey'),
    Rect (1800, 255, 40, 40, fill='darkGrey'),
    Rect (1900, 180, 40, 40, fill='darkGrey'),
    )
solarCourse2.rotateAngle = 0
solarCourse2.visible = False

solarCourse3 = Group (
    Rect (556, 180, 40, 40, fill='darkGrey'),
    Rect (650, 105, 40, 40, fill='darkGrey'),
    Rect (650, 255, 40, 40, fill='darkGrey'),
    Rect (800, 105, 40, 40, fill='darkGrey'),
    Rect (800, 255, 40, 40, fill='darkGrey'),
    Rect (900, 180, 40, 40, fill='darkGrey'),
    Rect (1100, 105, 40, 40, fill='darkGrey'),
    Rect (1100, 180, 40, 40, fill='darkGrey'),
    Rect (1320, 180, 40, 40, fill='darkGrey'),
    Rect (1320, 245, 40, 40, fill='darkGrey'),
    )
solarCourse3.visible = False
solarCourse3.rotateAngle = 0

solarBattery = Group ()
solarBatteryEmpty = Line (400, 375, 250, 375, lineWidth = 20, fill='grey')
solarBatteryPercentage = Line (400, 375, 300, 375, lineWidth = 20, fill='darkGrey')
solarBattery.add (
    solarBatteryEmpty,
    solarBatteryPercentage,
    Label ("BATTERY", 350, 350, size=15, font = 'montserrat', fill='white', bold=True)
    )
solarBattery.visible = False

solarFact1 = Group (
    Label ("Solar energy is the most", 200, 25, fill='white', font='montserrat', size=15, bold=True),
    Label ("abundant renewable energy source", 200, 50, fill='white', font='montserrat', size=15, bold=True)
    )
solarFact1.visible = False

solarFact2 = Group (
    Label ("Solar power is energy", 200, 25, fill='white', font='montserrat', size=15, bold=True),
    Label ('derived from the sun', 200, 50, fill='white', font='montserrat', size=15, bold=True),
    )
solarFact2.visible = False

solarFact3 = Group (
    Label ("Solar photovoltaic cells/panels convert sunlight", 200, 25, fill='white', font='montserrat', size=15, bold=True),
    Label ("into electricity using semiconductors and electrons", 200, 50, fill='white', font='montserrat', size=13, bold=True),
    )
solarFact3.visible = False

solarFact4 = Group (
    Label("Besides electricity, solar energy can", 200, 25, fill='white', font='montserrat', size=15, bold=True),
    Label("also be used for heating", 200, 50, fill='white', font='montserrat', size=15, bold=True)
    )
solarFact4.visible = False

solarFact5 = Group (
    Label ("India has the biggest photovoltaic plant in the world", 200, 25, fill='white', font='montserrat', size=13, bold=True),
    Label ("while China produces the most electricity (solar) in the world", 200, 50, fill='white', font='montserrat', size=12, bold=True)
    )
solarFact5.visible = False

solarFact6 = Group (
    Label ("Every second about half the Earth's surface recieves" , 200, 25, fill='white', font='montserrat', size=13, bold=True),
    Label ("sunlight, which can mostly be used to generate electricity", 200, 50, fill='white', font='montserrat', size=12, bold=True),
    )
solarFact6.visible = False

solarFact7 = Group (
    Label ("With much more advanced technologies, one hour of sunlight", 200, 25, fill='white', font='montserrat', size=12, bold=True),
    Label ("could power the entire world for one whole year", 200, 50, fill='white', font='montserrat', size=12, bold=True)
    )
solarFact7.visible = False

solarFact8 = Group (
    Label ("Solar thermal plants use the sunlight to heat liquids to", 200, 25, fill='white', font='montserrat', size=13, bold=True),
    Label ("produce steam which drives a turbine and generates electricity", 200, 50, fill='white', bold=True, font='montserrat', size=11)
    )
solarFact8.visible = False

solarFact9 = Group (
    Label ("Thermally activated cooling systems use solar thermal energy", 200, 25, fill='white', bold=True, font='montserrat', size=11),
    Label("to heat a special solution of refrigerant and absorbant", 200, 50, fill='white', font='montserrat', size=12, bold=True)
    )
solarFact9.visible = False

solarPowerQuestions = Group ()
solarQuestion1 = Label ('Solar power is energy derived from _______', 200, 120, size=13, font='montserrat', fill='white', bold=True)
solarQuestion2 = Label ('Solar energy is both light energy and _______ energy', 200, 160, size=13, font='montserrat', fill='white', bold=True)
solarQuestion3 = Label ('Every second about _______ of Earth recieves solar energy', 200, 200, size=12, font='montserrat', fill='white', bold=True)
solarQuestion4 = Label ('Solar energy is the most _______ renewable energy source', 200, 240, size=12, font='montserrat', fill='white', bold=True)
solarQuestion5 = Label ('Heat from the sun can be used to produce _______, power turbines, and generate electricity', 200, 280, size=7.5, font='montserrat', fill='white', bold=True)
solarPowerQuestions.add (
    solarQuestion1,
    solarQuestion2,
    solarQuestion3,
    solarQuestion4,
    solarQuestion5
    )
solarPowerQuestions.visible = False

solarPowerAnswers = Group()
solarAnswer1 = Label ('THE SUN', 80, 360, size=15, font='montserrat', fill='white', bold=True)
solarAnswer2 = Label ('HEAT', 300, 360, size=15, font='montserrat', fill='white', bold=True)
solarAnswer3 = Label ('HALF', 190, 360, size=15, font='montserrat', fill='white', bold=True)
solarAnswer4 = Label ('ABUNDANT', 140, 320, size=15, font='montserrat', fill='white', bold=True)
solarAnswer5 = Label ('STEAM', 250, 320, size=15, font='montserrat', fill='white', bold=True)
solarPowerAnswers.add (
    solarAnswer1,
    solarAnswer2,
    solarAnswer3,
    solarAnswer4,
    solarAnswer5,
    )
solarPowerAnswers.visible = False

### Wind Power Challenge Shapes

windPowerBackMountains = Group (
    Polygon(200, 80, 240, 90, 280, 85, 320, 140, 200, 140, fill='darkGrey'),
    Polygon(240, 90, 280, 85, 260, 140, fill='grey'),
    Polygon (80, 85, 110, 70, 120, 140, fill='grey'),
    Polygon(110, 70, 200, 80, 200, 140, 110, 140, fill='grey'),
    Polygon(0, 80, 40, 90, 80, 85, 120, 140, 0, 140, fill='grey'),
    Polygon(40, 90, 80, 85, 60, 140, fill='darkGrey'),
    Polygon (280, 85, 320, 140, 450, 140, fill='darkGrey'),
    Polygon (280, 85, 450, 85, 450, 140, fill='grey'),
    Rect (0, 300, 450, 50, fill='silver'),
    Polygon(0, 115, 30, 110, 80, 120, 140, 140, 180, 130, 240, 340, 0, 340, fill='silver'),
    Polygon (80, 120, 140, 140, 55, 340, fill='lightGrey'),
    Polygon (180, 130, 240, 340, 280, 340, 260, 130, fill='lightGrey'),
    Polygon (280, 340, 450, 340, 450, 110, 285, 120, 260, 130, fill='silver'),
    Polygon (450, 110, 450, 340, 345, 340, fill='lightGrey'),
    )
windPowerFrontMountains = Group (
    Polygon(200, 80, 240, 90, 280, 85, 320, 140, 200, 140, fill='lightSlateGrey'),
    Polygon(240, 90, 280, 85, 260, 140, fill='slateGrey'),
    Polygon (80, 85, 110, 70, 110, 140, fill='lightSlateGrey'),
    Polygon(0, 80, 40, 90, 80, 85, 120, 140, 0, 140, fill='lightSlateGrey'),
    Polygon(40, 90, 80, 85, 60, 140, fill='slateGrey'),
    Polygon (280, 85, 450, 85, 450, 140, 320, 160, fill='lightSlateGrey'),
    Polygon (110, 70, 200, 80, 200, 140, 110, 140, fill='lightSlateGrey')
    )
windPowerFrontMountains.centerY += 260
windPowerMountains = Group (windPowerBackMountains, windPowerFrontMountains)
windPowerMountains.visible = False

bird = Group (
    Line (188, 207, 174, 213, fill='gold', lineWidth=5),
    Line (198, 216, 183, 223, fill='gold', lineWidth=5),
    Circle (200, 200, 20, fill='mediumSeaGreen'),
    Circle (210, 185, 15, fill='yellowGreen'),
    Circle (215, 180, 3),
    Polygon (220, 183, 220, 193, 235, 187, fill='gold'),
    Polygon (185, 202, 205, 202, 195, 212, fill='darkSeaGreen', rotateAngle=35)
    )
bird.visible = False

windPowerObstacles1 = Group (
    Line (325, 400, 325, 280, lineWidth = 10, fill=rgb(161,161,161)),
    Star (325, 280, 60, 3, fill='gainsboro', roundness=20, rotateAngle=20),
    
    Line (400, 400, 400, 230, lineWidth = 10, fill=rgb(161,161,161)),
    Star (400, 230, 60, 3, fill='gainsboro', roundness=20, rotateAngle=20),
    
    Line (500, 400, 500, 250, lineWidth = 10, fill=rgb(161,161,161)),
    Star (500, 250, 60, 3, fill='gainsboro', roundness=20, rotateAngle=20),
    
    Line (625, 400, 625, 250, lineWidth = 10, fill=rgb(161,161,161)),
    Star (625, 250, 60, 3, fill='gainsboro', roundness=20, rotateAngle=20),
    
    Line (700, 400, 700, 200, lineWidth = 10, fill=rgb(161,161,161)),
    Star (700, 200, 60, 3, fill='gainsboro', roundness=20, rotateAngle=20),
    
    Line (800, 400, 800, 250, lineWidth = 10, fill=rgb(161,161,161)),
    Star (800, 250, 60, 3, fill='gainsboro', roundness=20, rotateAngle=20),
    
    Line (325 +600, 400, 325+600, 300, lineWidth = 10, fill=rgb(161,161,161)),
    Star (325+600, 300, 60, 3, fill='gainsboro', roundness=20, rotateAngle=20),
    
    Line (400+600, 400, 400+600, 230, lineWidth = 10, fill=rgb(161,161,161)),
    Star (400+600, 230, 60, 3, fill='gainsboro', roundness=20, rotateAngle=20),
    
    Line (500+600, 400, 500+600, 350, lineWidth = 10, fill=rgb(161,161,161)),
    Star (500+600, 350, 60, 3, fill='gainsboro', roundness=20, rotateAngle=20),
    
    Line (625+600, 400, 625+600, 250, lineWidth = 10, fill=rgb(161,161,161)),
    Star (625+600, 250, 60, 3, fill='gainsboro', roundness=20, rotateAngle=20),
    
    Line (700+600, 400, 700+600, 200, lineWidth = 10, fill=rgb(161,161,161)),
    Star (700+600, 200, 60, 3, fill='gainsboro', roundness=20, rotateAngle=20),
    
    Line (800+600, 400, 800+600, 250, lineWidth = 10, fill=rgb(161,161,161)),
    Star (800+600, 250, 60, 3, fill='gainsboro', roundness=20, rotateAngle=20),
    )
    
windPowerObstacles1.centerX = 1000
windPowerObstacles1.centerY +=150

windPowerObstacles2  = Group (
    Line (1190, 0, 1190, 155, lineWidth=10, fill='silver'),
    Star (1190, 165, 60, 3, fill='gainsboro', roundness=20, rotateAngle=50),
    
    Line (1300, 0, 1300, 155, lineWidth=10, fill='silver'),
    Star (1300, 165, 60, 3, fill='gainsboro', roundness=20, rotateAngle=50),
    
    Line (1400, 0, 1400, 170, lineWidth=10, fill='silver'),
    Star (1400, 180, 60, 3, fill='gainsboro', roundness=20, rotateAngle=50),
    
    Line (1550, 0, 1550, 180, lineWidth=10, fill='silver'),
    Star (1550, 190, 60, 3, fill='gainsboro', roundness=20, rotateAngle=50),
    
    Line (1680, 0, 1680, 200, lineWidth=10, fill='silver'),
    Star (1680, 210, 60, 3, fill='gainsboro', roundness=20, rotateAngle=50),
    
    Line (1770, 0, 1770, 260, lineWidth=10, fill='silver'),
    Star (1770, 270, 60, 3, fill='gainsboro', roundness=20, rotateAngle=50),
    
    Line (1830, 0, 1830, 155, lineWidth=10, fill='silver'),
    Star (1830, 165, 60, 3, fill='gainsboro', roundness=20, rotateAngle=50),
    )
    
windPowerObstacles2.centerX = 1000
windPowerObstacles2.centerY -=200

windPowerObstacles3_p1 = Group (
    Line (1190, 0, 1190, 155, lineWidth=10, fill='silver'),
    Star (1190, 165, 60, 3, fill='gainsboro', roundness=20, rotateAngle=50),
    
    Line (1550, 0, 1550, 180, lineWidth=10, fill='silver'),
    Star (1550, 190, 60, 3, fill='gainsboro', roundness=20, rotateAngle=50),
    
    Line (1670, 0, 1670, 155, lineWidth=10, fill='silver'),
    Star (1670, 165, 60, 3, fill='gainsboro', roundness=20, rotateAngle=50),
    
    Line (2100, 0, 2100, 175, lineWidth=10, fill='silver'),
    Star (2100, 185, 60, 3, fill='gainsboro', roundness=20, rotateAngle=50),
    )
    
windPowerObstacles3_p1.centerX = 1000
windPowerObstacles3_p1.centerY -=200

windPowerObstacles3_p2 = Group (
    Line (325, 400, 325, 280, lineWidth = 10, fill=rgb(161,161,161)),
    Star (325, 280, 60, 3, fill='gainsboro', roundness=20, rotateAngle=20),
    
    Line (625, 400, 625, 250, lineWidth = 10, fill=rgb(161,161,161)),
    Star (625, 250, 60, 3, fill='gainsboro', roundness=20, rotateAngle=20),
    
    Line (325 +600, 400, 325+600, 300, lineWidth = 10, fill=rgb(161,161,161)),
    Star (325+600, 300, 60, 3, fill='gainsboro', roundness=20, rotateAngle=20),
    
    Line (400+600, 400, 400+600, 230, lineWidth = 10, fill=rgb(161,161,161)),
    Star (400+600, 230, 60, 3, fill='gainsboro', roundness=20, rotateAngle=20),
    
    Line (500+600, 400, 500+600, 350, lineWidth = 10, fill=rgb(161,161,161)),
    Star (500+600, 350, 60, 3, fill='gainsboro', roundness=20, rotateAngle=20),
    
    Line (625+600, 400, 625+600, 250, lineWidth = 10, fill=rgb(161,161,161)),
    Star (625+600, 250, 60, 3, fill='gainsboro', roundness=20, rotateAngle=20),
    
     Line (800+600, 400, 800+600, 250, lineWidth = 10, fill=rgb(161,161,161)),
    Star (800+600, 250, 60, 3, fill='gainsboro', roundness=20, rotateAngle=20),
    )
    
windPowerObstacles3_p2.centerX = 1000
windPowerObstacles3_p2.centerY +=100

windFact1 = Group (
    Label ("Wind energy is actually a result", 200, 25, fill='white', font='montserrat', size=15, bold=True),
    Label ("of solar energy, or energy from the sun", 200, 50, fill='white', font='montserrat', size=15, bold=True)
    )
windFact1.visible = False

windFact2 = Group (
    Label ("Uneven heating in our atmosphere causes", 200, 25, fill='white', font='montserrat', size=15, bold=True),
    Label ("the movement of air, which creates wind", 200, 50, fill='white', font='montserrat', size=15, bold=True)
    )
windFact2.visible = False

windFact3 = Group (
    Label ("As long as our sun is around, wind", 200, 365, fill='white', font='montserrat', size=15, bold=True),
    Label ("energy will remain a sustainable resource", 200, 380, fill='white', font='montserrat', size=15, bold=True)
    )
windFact3.visible = False

windFact4 = Group (
    Label ("Today, wind energy is much cheaper to", 200, 365, fill='white', font='montserrat', size=15, bold=True),
    Label ("use compared to fossil fuel while being cleaner", 200, 380, fill='white', font='montserrat', size=15, bold=True)
    )
windFact4.visible = False

windFact5 = Group (
    Label ("Right now, wind farms are ideally in", 200, 365, fill='white', font='montserrat', size=15, bold=True),
    Label ("remote places, making transport harder", 200, 380, fill='white', font='montserrat', size=15, bold=True)
    )
windFact5.visible = False

windFact6 = Group (
    Label ("China and the USA produce the most wind", 200, 245, fill='white', font='montserrat', size=15, bold=True),
    Label ("electricity worldwide, collectively about 50%", 200, 260, fill='white', font='montserrat', size=15, bold=True)
    )
windFact6.visible = False

windPowerQuestions = Group ()
windQuestion1 = Label ('Wind farms are typically in _______ places', 200, 120, size=13, font='montserrat', fill='white', bold=True)
windQuestion2 = Label ('Wind is the result of _______ energy', 200, 160, size=13, font='montserrat', fill='white', bold=True)
windQuestion3 = Label ('Wind is a _______ source of energy', 200, 200, size=12, font='montserrat', fill='white', bold=True)
windQuestion4 = Label ('Today, wind energy is much _______ to harness', 200, 240, size=12, font='montserrat', fill='white', bold=True)
windQuestion5 = Label ('China and the USA generate about _______ of wind electricity', 200, 280, size=10, font='montserrat', fill='white', bold=True)
windPowerQuestions.add (
    windQuestion1,
    windQuestion2,
    windQuestion3,
    windQuestion4,
    windQuestion5
    )
windPowerQuestions.visible = False

windPowerAnswers = Group()
windAnswer1 = Label ('REMOTE', 300, 360, size=15, font='montserrat', fill='white', bold=True)
windAnswer2 = Label ('SOLAR', 80, 360, size=15, font='montserrat', fill='white', bold=True)
windAnswer3 = Label ('SUSTAINABLE', 140, 320, size=15, font='montserrat', fill='white', bold=True)
windAnswer4 = Label ('CHEAPER', 190, 360, size=15, font='montserrat', fill='white', bold=True)
windAnswer5 = Label ('50%', 250, 320, size=15, font='montserrat', fill='white', bold=True)
windPowerAnswers.add (
    windAnswer1,
    windAnswer2,
    windAnswer3,
    windAnswer4,
    windAnswer5,
    )
windPowerAnswers.visible = False

### Ozone Layer Shapes

ozonePlayer = Polygon (165, 390, 235, 390, 235, 370, 210, 370, 210, 360, 190, 360, 190, 370, 165, 370, fill='white')
ozonePlayer.centerY += 10
ozonePlayer.visible = False

ozoneEarth = Group (
    Arc (200, 0, 400, 100, 90, 180, fill='blue'),
    Oval (53, 5, 50, 30, fill='green', rotateAngle = 240),
    Oval (162, 11, 30, 40, fill='green', rotateAngle = 90),
    Oval (183, 0, 40, 50, fill='green', rotateAngle = 90),
    Oval (300, 5, 60, 30, fill='green', rotateAngle = 160)
    )
ozoneEarth.visible = False

ozoneInvaders = Group (
    Circle (50, 130, 10, fill='red'),
    Circle (80, 130, 10, fill='red'),
    Circle (110, 130, 10, fill='red'),
    Circle (140, 130, 10, fill='red'),
    Circle (170, 130, 10, fill='red'),
    Circle (200, 130, 10, fill='red'),
    Circle (50, 160, 10, fill='red'),
    Circle (80, 160, 10, fill='red'),
    Circle (110, 160, 10, fill='red'),
    Circle (140, 160, 10, fill='red'),
    Circle (170, 160, 10, fill='red'),
    Circle (200, 160, 10, fill='red'),
    )
ozoneInvaders.visible = False

ozoneBullet = Rect (ozonePlayer.centerX - 5, ozonePlayer.centerY - 40, 10, 20, fill='gold', visible = False)

ozoneFact1 = Group (
    Label ("The ozone layer is part of the atmosphere", 200, 75, fill='white', font='montserrat', size=15, bold=True),
    Label ("protecting Earth from harmful UV rays", 200, 100, fill='white', font='montserrat', size=15, bold=True)
    )
ozoneFact1.visible = False

ozoneFact2 = Group (
    Label ("UV rays, or Ultra Violet Radiation rays", 200, 75, fill='white', font='montserrat', size=15, bold=True),
    Label ("are emitted or sent by the sun", 200, 100, fill='white', font='montserrat', size=15, bold=True)
    )
ozoneFact2.visible = False

ozoneFact3 = Group (
    Label ("CFCs are chemicals used in many products such", 200, 75, fill='white', font='montserrat', size=15, bold=True),
    Label ("as aerosol spray, coolant, solvent and foam", 200, 100, fill='white', font='montserrat', size=15, bold=True)
    )
ozoneFact3.visible = False

ozoneFact4 = Group (
    Label ("While CFCs are not toxic, they release chemicals", 200, 75, fill='white', font='montserrat', size=15, bold=True),
    Label ("like Chlorine into the upper atmosphere", 200, 100, fill='white', font='montserrat', size=15, bold=True)
    )
ozoneFact4.visible = False

ozoneFact5 = Group (
    Label ("Just 1 atom of chorine is able to break", 200, 75, fill='white', font='montserrat', size=15, bold=True),
    Label ("down and destroy 100,000 ozone molecules", 200, 100, fill='white', font='montserrat', size=15, bold=True)
    )
ozoneFact5.visible = False

ozoneFact6 = Group (
    Label ("In 1987, 27 nations signed the Montreal Protocol,", 200, 75, fill='white', font='montserrat', size=15, bold=True),
    Label ("an agreement to reduce CFC production", 200, 100, fill='white', font='montserrat', size=15, bold=True)
    )
ozoneFact6.visible = False

ozoneFact7 = Group (
    Label ("Thanks to this agreement, ozone is now able to", 200, 75, fill='white', font='montserrat', size=15, bold=True),
    Label ("regenerate and should return to normal by 2060", 200, 100, fill='white', font='montserrat', size=15, bold=True)
    )
ozoneFact7.visible = False

ozoneLayerQuestions = Group ()
ozoneQuestion1 = Label ('1 Chlorine atom can break down _______ ozone molecules', 200, 120, size=10, font='montserrat', fill='white', bold=True)
ozoneQuestion2 = Label ('CFCs are used in products like aerosol _______', 200, 160, size=13, font='montserrat', fill='white', bold=True)
ozoneQuestion3 = Label ('_______ protects Earth from harmful UV Radiation', 200, 200, size=12, font='montserrat', fill='white', bold=True)
ozoneQuestion4 = Label ('Today, Ozone is expected to mostly recover by _______', 200, 240, size=12, font='montserrat', fill='white', bold=True)
ozoneQuestion5 = Label ('Ultra Violet Radiation is emitted by the _______', 200, 280, size=13, font='montserrat', fill='white', bold=True)
ozoneLayerQuestions.add (
    ozoneQuestion1,
    ozoneQuestion2,
    ozoneQuestion3,
    ozoneQuestion4,
    ozoneQuestion5
    )
ozoneLayerQuestions.visible = False

ozoneLayerAnswers = Group()
ozoneAnswer1 = Label ('100,000', 80, 360, size=15, font='montserrat', fill='white', bold=True)
ozoneAnswer2 = Label ('SPRAYS', 300, 360, size=15, font='montserrat', fill='white', bold=True)
ozoneAnswer3 = Label ('OZONE', 190, 360, size=15, font='montserrat', fill='white', bold=True)
ozoneAnswer4 = Label ('2060', 140, 320, size=15, font='montserrat', fill='white', bold=True)
ozoneAnswer5 = Label ('SUN', 250, 320, size=15, font='montserrat', fill='white', bold=True)
ozoneLayerAnswers.add (
    ozoneAnswer1,
    ozoneAnswer2,
    ozoneAnswer3,
    ozoneAnswer4,
    ozoneAnswer5,
    )
ozoneLayerAnswers.visible = False

### Ecosystem Shapes

frog = Group (
    Polygon (195, 215, 205, 215, 215, 265, 185, 265, fill='darkGreen'),
    Oval (200, 200, 60, 50, fill='green'),
    Oval (175, 180, 25, 25, fill='green'),
    Oval (225, 180, 25, 25, fill='green'),
    Circle (175, 180, 8, fill='white'),
    Circle (225, 180, 8, fill='white'),
    Arc (200, 205, 20, 20, 90, 180, fill='darkGreen')
    )
frogEye = Group (
    Circle (175, 180, 5, fill='black'),
    Circle (225, 180, 5, fill='black'),
    )
frog.add(frogEye)
frog.centerY = 375
frog.visible = False

ecoCloud1 = Group (
    Circle(40, 60, 20, fill='white'),
    Circle(70, 50, 30, fill='white'),
    Circle(90, 65, 20, fill='white'),
)
ecoCloud1.centerY += 175

ecoCloud2 = Group (    
    Circle(265, 160, 20, fill='white'),
    Circle(290, 150, 30, fill='white'),
    )
    
ecoClouds = Group (
    ecoCloud1,
    ecoCloud2,
    )
ecoClouds.visible = False

frogTongue = Line(200, 370, 200, 180, fill='pink', lineWidth = 10)
frogTongue.visible = False

ecoH1 = Circle(285, 380, 10, fill='red')
ecoH2 = Circle(310, 380, 10, fill='red')
ecoH3 = Circle(335, 380, 10, fill='red')
ecoH4 = Circle(360, 380, 10, fill='red')
ecoH5 = Circle(385, 380, 10, fill='red')
ecoHearts = Group (
    ecoH1,
    ecoH2,
    ecoH3,
    ecoH4,
    ecoH5
    )
ecoHearts.visible = False

cursor = Group(
    Circle(200, 200, 20, fill="darkRed"),
    Circle(200, 200, 10, fill="red", border='white', borderWidth=5)
    )
cursor.visible = False

ecoFlies = Group()

ecoFact1 = Group (
    Label ("An ecosystem is an area where organisms,", 200, 45, fill='white', font='montserrat', size=15, bold=True),
    Label ("weather and geography form a bubble of life", 200, 70, fill='white', font='montserrat', size=15, bold=True)
    )
ecoFact1.visible = False

ecoFact2 = Group (
    Label ("An ecosystem contains both biotic and", 200, 45, fill='white', font='montserrat', size=15, bold=True),
    Label ("abiotic factors", 200, 70, fill='white', font='montserrat', size=15, bold=True)
    )
ecoFact2.visible = False

ecoFact3 = Group (
    Label ("Biotic factors are living organisms", 200, 45, fill='white', font='montserrat', size=15, bold=True),
    Label ("like animals and plants", 200, 70, fill='white', font='montserrat', size=15, bold=True)
    )
ecoFact3.visible = False

ecoFact4 = Group (
    Label ("Abiotic factors are non-living parts like rocks,", 200, 45, fill='white', font='montserrat', size=15, bold=True),
    Label ("rivers or even weather, terrain and climate", 200, 70, fill='white', font='montserrat', size=15, bold=True)
    )
ecoFact4.visible = False

ecoFact5 = Group (
    Label ("Every factor in a ecosystem is linked,", 200, 45, fill='white', font='montserrat', size=15, bold=True),
    Label ("existing in a delicate balance", 200, 70, fill='white', font='montserrat', size=15, bold=True)
    )
ecoFact5.visible = False

ecoFact6 = Group (
    Label ("For example, temperature changes plant growth", 200, 45, fill='white', font='montserrat', size=15, bold=True),
    Label ("which affects a vital food source for herbivores,", 200, 70, fill='white', font='montserrat', size=15, bold=True),
    Label ("whom serve as a food source to predators", 200, 95, fill='white', font='montserrat', size=15, bold=True)
    )
ecoFact6.visible = False

ecoFact7 = Group (
    Label ("Too many predators, too many plant eating", 200, 45, fill='white', font='montserrat', size=15, bold=True),
    Label ("animals or irregular weather can break the balance", 200, 70, fill='white', font='montserrat', size=13, bold=True),
    )
ecoFact7.visible = False

ecoFact8 = Group (
    Label ("As human populations have increased,", 200, 45, fill='white', font='montserrat', size=15, bold=True),
    Label ("ecosystems have become overun and destroyed", 200, 70, fill='white', font='montserrat', size=15, bold=True),
    )
ecoFact8.visible = False

ecoFact9 = Group (
    Label ("This is due to activities like deforestation,", 200, 45, fill='white', font='montserrat', size=15, bold=True),
    Label ("climate change, pollution and more", 200, 70, fill='white', font='montserrat', size=15, bold=True),
    )
ecoFact9.visible = False

ecoFact10 = Group (
    Label ("While slow, ecosystems can recover, however", 200, 45, fill='white', font='montserrat', size=15, bold=True),
    Label ("issues related to ecosystem loss remain today", 200, 70, fill='white', font='montserrat', size=15, bold=True),
    )
ecoFact10.visible = False

ecosystemQuestions = Group ()
ecoQuestion1 = Label ('Ecosystems contain _______ and abiotic factors', 200, 120, size=13, font='montserrat', fill='white', bold=True)
ecoQuestion2 = Label ('Ecosystems rely on a delicate _______', 200, 160, size=13, font='montserrat', fill='white', bold=True)
ecoQuestion3 = Label ('_______ factors are non-living parts', 200, 200, size=13, font='montserrat', fill='white', bold=True)
ecoQuestion4 = Label ('Leading causes of ecosystem loss include _______', 200, 240, size=13, font='montserrat', fill='white', bold=True)
ecoQuestion5 = Label ("An _______ consists of organisms, climate and geography", 200, 280, size=11, font='montserrat', fill='white', bold=True)
ecosystemQuestions.add (
    ecoQuestion1,
    ecoQuestion2,
    ecoQuestion3,
    ecoQuestion4,
    ecoQuestion5
    )
ecosystemQuestions.visible = False

ecosystemAnswers = Group()
ecoAnswer1 = Label ('BIOTIC', 80, 360, size=15, font='montserrat', fill='white', bold=True)
ecoAnswer2 = Label ('BALANCE', 300, 360, size=15, font='montserrat', fill='white', bold=True)
ecoAnswer3 = Label ('ABIOTIC', 190, 360, size=15, font='montserrat', fill='white', bold=True)
ecoAnswer4 = Label ('CLIMATE CHANGE', 120, 320, size=15, font='montserrat', fill='white', bold=True)
ecoAnswer5 = Label ('ECOSYSTEM', 270, 320, size=15, font='montserrat', fill='white', bold=True)
ecosystemAnswers.add (
    ecoAnswer1,
    ecoAnswer2,
    ecoAnswer3,
    ecoAnswer4,
    ecoAnswer5,
    )
ecosystemAnswers.visible = False

### Functions

def backgroundMusic():
    if (app.status == 'intro'):
        menuTrack.play(loop=True)
        if (introTagline.size < 15):
            introTagline.size += 0.5
    elif (app.status == 'menu'):
        menuTrack.play(loop=True)
        menuBadgeAnimation()
    else:
        menuTrack.pause()
    
    if (app.status == 'solarChallenge'):
        solarMusic.play(loop=True)
    else:
        solarMusic.pause()
    
    if (app.status == 'geoChallenge'):
        geoThermalMusic.play(loop=True)
    else:
        geoThermalMusic.pause()
        
    if (app.status == 'windChallenge'):
        windMusic.play(loop=True)
    else:
        windMusic.pause()
    
    if (app.status == 'ozoneChallenge'):
        ozoneMusic.play(loop=True)
    else:
        ozoneMusic.pause()
        
    if (app.status == 'ecosystemChallenge'):
        ecoMusic.play(loop=True)
    else:
        ecoMusic.pause()
    
    if (app.status == 'trophy'):
        finalTrack.play(loop=True)
    else:
        finalTrack.pause()

def onStep():
    message.toFront()
    backgroundMusic()
    if ((app.message == True) and (message.centerY <= 30)):
        message.centerY += 3
    elif (app.message == True):
        if (app.messageTimer>=0):
            app.messageTimer -= 1
        else:
            app.messageTimer = 90
            message.centerY = -50
            message.visible = False
            app.message = False
            messageLabel.value = ''
    loadingTrees.centerY += 10
    loadingTrees.toFront()
    if (loadingTrees.top >= 400):
        loadingTrees.clear()
        loadingScreen.centerY = -500
        loadingSquare.visible = False
    if (app.status == 'trophy'):
        winEffect.visible = True
        trophy1.rotateAngle += 5
        trophy2.rotateAngle -= 5
        trophy3.rotateAngle += 3
        trophy4.rotateAngle += 3
        trophy5.rotateAngle -= 4
    else:
        winEffect.visible = False
    if ((app.geoTherm == True and app.solarPower == True and app.windPower == True and app.ozoneLayer == True and app.ecosystem == True) or app.devHack==True):
        if app.status == 'menu' and menu.visible == True:
            if trophyLabel.value != "???..." and trophyLabel.value != "CERTIFICATE":
                trophyLabel.value = "???..."
                trophyLabel.fill='white'
                trophyBadgePart.fill='white'
                trophyBadgePart.border = 'darkKhaki'
                trophyBadgePart2.fill='gold'
                trophyBadgePart3.border='gold'
                trophyBadgePart4.opacity = 100
    ### Geo Challenge onStep()         
    if (app.geoChallenge == True):
        geoThermStart.toFront()
        message.toFront()
        if (geoPipe2.centerY >= 380):
            if (app.geoStage == 0):
                broadcastMessage('| Avoid the obstacles |', '| Pay attention, you will be quizzed on the facts |')
                app.geoStage = 1
                geoThermStart.visible = False
                geoPipe.y1 = -10
                geoPipe.y2 = 90
                geoPipe2.centerY = 90
                geoThermCourse1.visible = True
                geoPipe.toFront()
                geoPipe2.toFront()
                geoFact1.visible = True
                geoFact1.toFront()
            elif (app.geoStage == 1):
                app.geoStage = 2
                geoPipe.y1 = -10
                geoPipe.y2 = 90
                geoPipe2.centerY = 90
                geoThermCourse2.visible = True
                geoThermCourse1.visible = False
                geoPipe.toFront()
                geoPipe2.toFront()
                geoFact2.visible = True
                geoFact1.visible = False
                geoFact2.toFront()
            elif (app.geoStage == 2):
                app.geoStage = 3
                geoPipe.y1 = -10
                geoPipe.y2 = 90
                geoPipe2.centerY = 90
                geoThermCourse3.visible = True
                geoThermCourse2.visible = False
                geoPipe.toFront()
                geoPipe2.toFront()
                geoFact3.visible = True
                geoFact2.visible = False
                geoFact3.toFront()
            elif (app.geoStage == 3):
                app.geoStage = 4
                geoPipe.y1 = -10
                geoPipe.y2 = 90
                geoPipe2.centerY = 90
                geoThermCourse4.visible = True
                geoThermCourse3.visible = False
                geoPipe.toFront()
                geoPipe2.toFront()
                geoFact4.visible = True
                geoFact3.visible = False
                geoFact4.toFront()
            elif (app.geoStage == 4):
                app.geoStage = 5
                geoPipe.y1 = -10
                geoPipe.y2 = 90
                geoPipe2.centerY = 90
                geoThermCourse5.visible = True
                geoThermCourse5p2.visible = True
                geoThermCourse4.visible = False
                geoPipe.toFront()
                geoPipe2.toFront()
                geoFact5.visible = True
                geoFact4.visible = False
                geoFact5.toFront()
            elif (app.geoStage == 5):
                geoFact5.visible = False
                geoThermCourse5.visible = False
                geoThermCourse5p2.visible = False
                app.geoStage = 6
                geoPipe.visible = False
                geoPipe2.visible = False
                geoPipe.y1 = -10
                geoPipe.y2 = 90
                geoPipe2.centerY = 90
                broadcastMessage('| Drag the answers and fill in the blanks |', '')
                geoThermQuestions.visible = True
                geoThermAnswers.visible = True
                if ((app.geoScore == 5) and (app.status == 'geoChallenge') and (app.geoStage == 6)):
                    menu.visible = True
                    geoThermQuestions.visible = False
                    geoThermAnswers.visible = False
                    geoThermPart4.visible = False
                    geoPipe.visible = False
                    geoPipe2.visible = False
                    app.background = 'green'
                    geoThermBadgePart.fill = 'white'
                    geoThermBadgePart.border = 'gainsboro'
                    geoThermLabel.fill='white'
                    geoThermPart2.fill='orange'
                    geoThermPart3.fill='yellow'
                    app.geoChallenge = False
                    geoThermStart.visible = False
                    broadcastMessage ('| GEOTHERMAL Badge Earned, Congrats! |', '')
                    app.status = 'menu'
                    app.geoChallenge = False
                    app.geoTherm  = True
        if (app.geoStage == 3):
            if (geoThermCourse3.centerX <= -300):
                geoThermCourse3.centerX = 700
            else:
                geoThermCourse3.centerX -= 10
        if (app.geoStage == 4):
            #pass
            geoThermCourse4.rotateAngle += 2
        if (app.geoStage == 5):
            if (geoThermCourse5p2.movement == 'Up'):
                geoThermCourse5p2.centerY -= 5
                if (geoThermCourse5p2.top <= 0):
                    geoThermCourse5p2.movement = 'Down'
            elif (geoThermCourse5p2.movement == 'Down'):
                geoThermCourse5p2.centerY += 5
                if (geoThermCourse5p2.bottom >= 400):
                    geoThermCourse5p2.movement = 'Up'
        if ((geoThermCourse2.movement=='left') and (app.geoStage == 2)):
            geoThermCourse2.centerX -= 10
            if (geoThermCourse2.centerX <= -200):
                geoThermCourse2.movement = 'right'
        elif ((geoThermCourse2.movement=='right') and (app.geoStage == 2)):
            geoThermCourse2.centerX += 10
            if (geoThermCourse2.centerX >= 500):
                geoThermCourse2.movement = 'left'
        if ((geoThermCourse1.hitsShape(geoPipe2)) and (app.geoStage == 1)):
            geoThermStart.visible = False
            geoPipe.y1 = -10
            geoPipe.y2 = 90
            geoPipe2.centerY = 90
            geoThermCourse1.visible = True
            geoPipe.toFront()
            geoPipe2.toFront()
            geoFact1.visible = True
            geoFact1.toFront()
        elif ((geoThermCourse2.hitsShape(geoPipe2)) and (app.geoStage == 2)):
            geoPipe.y1 = -10
            geoPipe.y2 = 90
            geoPipe2.centerY = 90
            geoThermCourse2.visible = True
            geoThermCourse1.visible = False
            geoPipe.toFront()
            geoPipe2.toFront()
            geoFact2.visible = True
            geoFact2.toFront()
        elif ((geoThermCourse3.hitsShape(geoPipe2)) and (app.geoStage == 3)):
            geoPipe.y1 = -10
            geoPipe.y2 = 90
            geoPipe2.centerY = 90
            geoThermCourse3.visible = True
            geoThermCourse2.visible = False
            geoPipe.toFront()
            geoPipe2.toFront()
            geoFact3.visible = True
            geoFact3.toFront()
        elif ((geoThermCourse4.hitsShape(geoPipe2)) and (app.geoStage == 4)):
            geoPipe.y1 = -10
            geoPipe.y2 = 90
            geoPipe2.centerY = 90
            geoThermCourse4.visible = True
            geoThermCourse3.visible = False
            geoPipe.toFront()
            geoPipe2.toFront()
            geoFact4.visible = True
            geoFact4.toFront()
        elif ((geoThermCourse5.hitsShape(geoPipe2)) and (app.geoStage == 5)):
            geoPipe.y1 = -10
            geoPipe.y2 = 90
            geoPipe2.centerY = 90
            geoThermCourse5.visible = True 
            geoPipe.toFront()
            geoPipe2.toFront()
            geoFact5.visible = True
            geoFact5.toFront()
        elif ((geoThermCourse5p2.hitsShape(geoPipe2)) and (app.geoStage == 5)):
            geoPipe.y1 = -10
            geoPipe.y2 = 90
            geoPipe2.centerY = 90
            geoThermCourse5.visible = True
            geoThermCourse4.visible = False
            geoPipe.toFront()
            geoPipe2.toFront()
            geoFact5.visible = True
            geoFact5.toFront()
    ### Solar Challenge onStep()     
    if (app.solarChallenge == True):
        if (solarCar.centerX <= 50):
            app.solarThrust = 0
        if (app.solarFact < 10):
            solarLine1.centerX -= app.solarThrust
            solarCourse1.centerX -= app.solarThrust
            solarCourse2.centerX -= app.solarThrust
            solarCourse3.centerX -= app.solarThrust
            solarOrb.centerX -= app.solarThrust
        if ((solarLine1.centerX <= 0) and (app.solarThrust > 0)):
            solarLine1.centerX = 400
        if ((solarLine1.centerX >= 400) and (app.solarThrust < 0)):
            solarLine1.centerX = 0
        if ((solarCar.hitsShape(solarCourse1)) and (app.solarFact < 4) and (solarCourse1.visible == True)):
            sleep(1)
            solarTrack1.centerX = 210
            solarLine1.centerX = 400
            solarCar.centerX = 40
            app.solarThrust = 0
            solarCourse1.centerX = 1148
            solarCar.centerY = 200
            solarOrbNext()
            app.solarBattery -= 1
        elif ((solarCar.hitsShape(solarCourse2)) and (app.solarFact < 7) and (solarCourse2.visible == True)):
            sleep(1)
            solarTrack1.centerX = 210
            solarLine1.centerX = 400
            solarCar.centerX = 40
            app.solarThrust = 0
            solarCourse2.centerX = 1148
            solarCar.centerY = 200
            solarOrbNext()
            app.solarBattery -= 1
        elif ((solarCar.hitsShape(solarCourse3)) and (app.solarFact < 10) and (solarCourse3.visible == True)):
            sleep(1)
            solarTrack1.centerX = 210
            solarLine1.centerX = 400
            solarCar.centerX = 40
            app.solarThrust = 0
            solarCourse3.centerX = 948
            solarCar.centerY = 200
            solarOrbNext()
            app.solarBattery -= 1
        if ((solarTrack1.containsShape(solarCar)) or (app.solarThrust == 0)):
            pass
        else:
            sleep(1)
            solarTrack1.centerX = 210
            solarLine1.centerX = 400
            solarCar.centerX = 40
            app.solarThrust = 0
            solarCourse1.centerX = 1148
            solarCourse2.centerX = 1148
            solarCourse3.centerX = 998
            solarCar.centerY = 200
            solarOrbNext()
            app.solarBattery -= 1
        if ((solarCourse1.right < -100) and (app.solarFact < 4) and (solarCourse1.visible == True)):
            solarCourse1.centerX = 1148
            solarCourse1.rotateAngle += 180
            nextSolarFact()
        elif ((solarCourse2.right < -100) and (app.solarFact < 7) and (solarCourse2.visible == True)):
            solarCourse2.centerX = 1148
            solarCourse2.rotateAngle += 180
            nextSolarFact()
        elif ((solarCourse3.right < -100) and (app.solarFact < 10) and (solarCourse3.visible == True)):
            solarCourse3.centerX = 998
            solarCourse3.rotateAngle += 180
            nextSolarFact()
        if (app.solarFact > 3):
            solarCourse1.visible = False
            solarCourse2.visible = True
        if (app.solarFact > 6):
            solarCourse2.visible = False
            solarCourse3.visible = True
        if (solarOrb.centerX <= -100):
            solarOrbNext()
        if ((solarCar.hitsShape(solarOrb)) and (solarOrb.visible == True)):
            solarOrb.visible = False
            if (app.solarBattery < 15):
                app.solarBattery += 1
        if (app.solarFact < 10):
            solarBatteryPercentage.x2 = 400 - (app.solarBattery*10)
            app.solarBattery -= app.solarThrust/650
        if (app.solarBattery <= 0):
            broadcastMessage('| You ran out of battery! Do not run into ', 'obstacles and collect orbs for battery |')
            app.solarFact = 1
            app.solarBattery = 7
            if (solarFact1.visible == True):
                solarFact1.visible = False
            if (solarFact2.visible == True):
                solarFact2.visible = False
            if (solarFact3.visible == True):
                solarFact3.visible = False
            if (solarFact4.visible == True):
                solarFact4.visible = False
            if (solarFact5.visible == True):
                solarFact5.visible = False
            if (solarFact6.visible == True):
                solarFact6.visible = False
            if (solarFact7.visible == True):
                solarFact7.visible = False
            if (solarFact8.visible == True):
                solarFact8.visible = False
            if (solarFact9.visible == True):
                solarFact9.visible = False
            solarFact1.visible = True
            solarTrack1.centerX = 210
            solarLine1.centerX = 400
            solarCar.centerX = 40
            app.solarThrust = 0
            solarCourse1.centerX = 1148
            solarCourse2.centerX = 1148
            solarCourse3.centerX = 958
            solarCar.centerY = 200
            solarCourse1.visible = True
            solarCourse2.visible = False
            solarCourse3.visible = False
            solarOrbNext()
    ### Wind Challenge onStep()
    if (app.windChallenge == True):
        if (app.windGravity == True):
            bird.centerY += 5
            bird.centerY += ((400-bird.centerY)/80)
            windPowerObstacles1.toFront()
            windPowerObstacles2.toFront()
            if ((app.windThrust == True) and (app.windGravity == True)):
                if (app.windFact < 3):
                    windPowerObstacles1.centerX -= 5
                    if (windPowerObstacles1.centerX<=-655):
                        app.windFact += 1
                        windPowerObstacles1.centerX = 1000
                        windPowerObstacles1.centerY -=50
                        if app.windFact == 1:
                            broadcastMessage("| Pay attention to the facts |", "| You will be quizzed at the end |")
                        if (app.windFact >= 3):
                            windPowerObstacles1.visible = False
                            windPowerObstacles2.visible = True
                    if (windPowerObstacles1.hitsShape(bird)):
                        app.windThrust = False
                elif (app.windFact < 6):
                    windPowerObstacles2.centerX -= 5
                    if (windPowerObstacles2.centerX<=-655):
                        app.windFact += 1
                        windPowerObstacles2.centerX = 1000
                        windPowerObstacles2.centerY +=50
                        if (app.windFact >= 6):
                            windPowerObstacles2.visible = False
                            windPowerObstacles3_p1.visible = True
                            windPowerObstacles3_p2.visible = True
                    if (windPowerObstacles2.hitsShape(bird)):
                        app.windThrust = False
                elif (app.windFact < 11):
                    windPowerObstacles3_p1.centerX -= 5
                    windPowerObstacles3_p2.centerX -= 5
                    windPowerObstacles3_p1.toFront()
                    windPowerObstacles3_p2.toFront()
                    if (windPowerObstacles3_p1.centerX<=-655):
                        app.windFact += 1
                        windPowerObstacles3_p1.centerX = 1000
                        windPowerObstacles3_p1.centerY +=20 
                        windPowerObstacles3_p2.centerX = 1000
                        windPowerObstacles3_p2.centerY -=20 
                        if (app.windFact >= 11):
                            if (app.windPower == False):
                                windPowerObstacles3_p1.visible = False
                                windPowerObstacles3_p2.visible = False
                                windPowerMountains.visible = False
                                bird.visible = False
                                app.windGravity = False
                                app.windThrust = False
                                windPowerQuestions.visible = True
                                windPowerAnswers.visible = True
                                broadcastMessage('| Drag the answers and fill in the blanks |', '')
                            else:
                                menu.visible = True
                                app.background = 'green'
                                windPowerObstacles3_p1.visible = False
                                windPowerObstacles3_p2.visible = False
                                windPowerMountains.visible = False
                                bird.visible = False
                                app.windGravity = False
                                app.windThrust = False
                                app.windChallenge = False
                                broadcastMessage ('| WIND Badge Earned, Congrats! |', '')
                                app.status = 'menu'
                            
                    if (windPowerObstacles3_p1.hitsShape(bird)) or (windPowerObstacles3_p2.hitsShape(bird)):
                        app.windThrust = False
        if ((app.windThrust == False) and (app.windGravity == True) and (bird.centerY < 550)):
            bird.rotateAngle += 5
        if (bird.centerY >= 550):
            app.windGravity = False
            bird.centerX = 200
            bird.centerY = 200
            bird.rotateAngle = 0
            windPowerObstacles1.centerX = 1000
            windPowerObstacles2.centerX = 1000
            windPowerObstacles3_p1.centerX = 1000
            windPowerObstacles3_p2.centerX = 1000
            windPowerObstacles1.centerY = 421.8
            windPowerObstacles2.centerY = -35.5
            windPowerObstacles3_p1.centerY = -75.5
            windPowerObstacles3_p2.centerY = 386.8
            app.windFact = 0
            windPowerObstacles2.visible = False
            windPowerObstacles3_p1.visible = False
            windPowerObstacles3_p2.visible = False
            windPowerObstacles1.visible = True
            app.windThrust = True
            app.windThrustTimer = 60
        
        if app.windFact > 0:
            if app.windFact == 1:
                windFact1.visible = True
                windFact2.visible = False
                windFact3.visible = False
                windFact4.visible = False
                windFact5.visible = False
                windFact6.visible = False
            elif app.windFact == 2:
                windFact1.visible = False
                windFact2.visible = True
                windFact3.visible = False
                windFact4.visible = False
                windFact5.visible = False
                windFact6.visible = False
            elif app.windFact == 3:
                windFact1.visible = False
                windFact2.visible = False
                windFact3.visible = True
                windFact4.visible = False
                windFact5.visible = False
                windFact6.visible = False
            elif app.windFact == 4:
                windFact1.visible = False
                windFact2.visible = False
                windFact3.visible = False
                windFact4.visible = True
                windFact5.visible = False
                windFact6.visible = False
            elif app.windFact == 5:
                windFact1.visible = False
                windFact2.visible = False
                windFact3.visible = False
                windFact4.visible = False
                windFact5.visible = True
                windFact6.visible = False
            elif app.windFact == 6:
                windFact1.visible = False
                windFact2.visible = False
                windFact3.visible = False
                windFact4.visible = False
                windFact5.visible = False
                windFact6.visible = True
            elif app.windFact == 7:
                windFact1.visible = False
                windFact2.visible = False
                windFact3.visible = False
                windFact4.visible = False
                windFact5.visible = False
                windFact6.visible = False
        else:
            windFact1.visible = False
            windFact2.visible = False
            windFact3.visible = False
            windFact4.visible = False
            windFact5.visible = False
            windFact6.visible = False

### Ozone Layer onStep()
    if (app.status == 'ozoneChallenge' or app.ozoneChallenge == True):
        if (ozoneBullet.visible == True):
            ozoneBullet.centerY -= 10
            if (ozoneBullet.hitsShape(ozoneInvaders)):
                if ozoneInvaders.hitTest(ozoneBullet.centerX, ozoneBullet.centerY) != None:
                    ozoneInvaders.remove(ozoneInvaders.hitTest(ozoneBullet.centerX, ozoneBullet.centerY))
                    ozoneBullet.visible = False
                elif ozoneInvaders.hitTest(ozoneBullet.centerX, ozoneBullet.centerY - 10) != None:
                    #print(ozoneInvaders.hitTest(ozoneBullet.centerX, ozoneBullet.centerY - 10) != "None")
                    ozoneInvaders.remove(ozoneInvaders.hitTest(ozoneBullet.centerX, ozoneBullet.centerY - 10))
                    ozoneBullet.visible = False
                elif ozoneInvaders.hitTest(ozoneBullet.centerX - 5, ozoneBullet.centerY) != None:
                    #print(ozoneInvaders.hitTest(ozoneBullet.centerX, ozoneBullet.centerY - 10) != "None")
                    ozoneInvaders.remove(ozoneInvaders.hitTest(ozoneBullet.centerX - 5, ozoneBullet.centerY))
                    ozoneBullet.visible = False
                elif ozoneInvaders.hitTest(ozoneBullet.centerX + 5, ozoneBullet.centerY) != None:
                    #print(ozoneInvaders.hitTest(ozoneBullet.centerX, ozoneBullet.centerY - 10) != "None")
                    ozoneInvaders.remove(ozoneInvaders.hitTest(ozoneBullet.centerX + 5, ozoneBullet.centerY))
                    ozoneBullet.visible = False
                else:
                    pass
            if (ozoneBullet.bottom <= 0):
                ozoneBullet.visible = False
        if (len(ozoneInvaders.children) > 0):
            if ozoneInvaders.right >= 380:
                app.ozoneInvaderDirection = -1
                ozoneInvaders.centerY += 15
            if ozoneInvaders.left <= 20:
                app.ozoneInvaderDirection = 1
                ozoneInvaders.centerY += 15
            if ozoneInvaders.bottom >= 350:
                resetOzone()
            ozoneInvaders.centerX += app.ozoneInvaderDirection*0.8
            
        else:
            if (app.ozoneFact <= 7):
                app.ozoneFact += 1
                resetOzone()
                
                if app.ozoneFact == 1:
                    ozoneFact1.visible = True
                    ozoneFact2.visible = False
                    ozoneFact3.visible = False
                    ozoneFact4.visible = False
                    ozoneFact5.visible = False
                    ozoneFact6.visible = False
                    ozoneFact7.visible = False
                elif app.ozoneFact == 2:
                    ozoneFact1.visible = False
                    ozoneFact2.visible = True
                    ozoneFact3.visible = False
                    ozoneFact4.visible = False
                    ozoneFact5.visible = False
                    ozoneFact6.visible = False
                    ozoneFact7.visible = False
                elif app.ozoneFact == 3:
                    ozoneFact1.visible = False
                    ozoneFact2.visible = False
                    ozoneFact3.visible = True
                    ozoneFact4.visible = False
                    ozoneFact5.visible = False
                    ozoneFact6.visible = False
                    ozoneFact7.visible = False
                elif app.ozoneFact == 4:
                    ozoneFact1.visible = False
                    ozoneFact2.visible = False
                    ozoneFact3.visible = False
                    ozoneFact4.visible = True
                    ozoneFact5.visible = False
                    ozoneFact6.visible = False
                    ozoneFact7.visible = False
                elif app.ozoneFact == 5:
                    ozoneFact1.visible = False
                    ozoneFact2.visible = False
                    ozoneFact3.visible = False
                    ozoneFact4.visible = False
                    ozoneFact5.visible = True
                    ozoneFact6.visible = False
                    ozoneFact7.visible = False
                elif app.ozoneFact == 6:
                    ozoneFact1.visible = False
                    ozoneFact2.visible = False
                    ozoneFact3.visible = False
                    ozoneFact4.visible = False
                    ozoneFact5.visible = False
                    ozoneFact6.visible = True
                    ozoneFact7.visible = False
                elif app.ozoneFact == 7:
                    ozoneFact1.visible = False
                    ozoneFact2.visible = False
                    ozoneFact3.visible = False
                    ozoneFact4.visible = False
                    ozoneFact5.visible = False
                    ozoneFact6.visible = False
                    ozoneFact7.visible = True
                    
        if (app.ozoneFact == 8):
            if (app.ozoneScore == 5):
                menu.visible = True
                ozoneLayerQuestions.visible = False
                ozoneLayerAnswers.visible = False
                ozonePart4.visible = False
                app.background = 'green'
                ozoneBadgePart.fill = 'white'
                ozoneBadgePart.border = 'gainsboro'
                ozoneLabel.fill='white'
                ozonePart2.fill='skyBlue'
                ozonePart3.fill='seaGreen'
                app.ozoneChallenge = False
                broadcastMessage ('| OZONE Badge Earned, Congrats! |', '')
                app.status = 'menu'
                app.ozoneLayer  = True
### Ecosystem onStep()

    if (app.ecosystemChallenge == True):
        for i in ecoFlies:
            if i.left >= 410:
                app.ecoFliesPast += 1
                app.ecoFlyCount += 1
                ecoFlies.remove(i)
                
                if app.ecoFliesPast == 1:
                    ecoH1.visible = False
                if app.ecoFliesPast == 2:
                    ecoH1.visible = False
                    ecoH2.visible = False
                if app.ecoFliesPast == 3:
                    ecoH1.visible = False
                    ecoH2.visible = False
                    ecoH3.visible = False
                if app.ecoFliesPast == 4:
                    ecoH1.visible = False
                    ecoH2.visible = False
                    ecoH3.visible = False
                    ecoH4.visible = False
                if app.ecoFliesPast == 5:
                    ecoHearts.visible = True
                    ecoH1.visible = True
                    ecoH2.visible = True
                    ecoH3.visible = True
                    ecoH4.visible = True
                    app.ecoFliesPast = 0
                    app.ecoFlyCount = 0
                    ecoFlies.clear()
                    cursor.centerX = 200
                    cursor.centerY = 200
                    broadcastMessage("Oops! You ran out of lives!", "Aim with your mouse and click to attack!")
                    app.ecoFlyTimer = 200
                
        ecoCloud1.centerX -= 3
        ecoCloud2.centerX += 3
        ecoClouds.toBack()
        if ecoCloud1.right <= -100:
            ecoCloud1.centerX = 500
        if ecoCloud2.left >= 700:
            ecoCloud2.centerX = -100
        if (app.ecoFlyTimer <= 0 and app.ecoFlyCount < 35):
            newFly = Group(
                Oval(280, 180, 25, 15, fill='black'),
                Oval(273, 172, 15, 10, fill='white', opacity = 50, rotateAngle = 40),
                Oval(280, 172, 15, 10, fill='white', opacity = 50, rotateAngle = 40),
            )
            newFly.centerX = -100
            newFly.centerY = random.randint(120, 270)
            ecoFlies.add (
                newFly
                )
            app.ecoFlyTimer = 120
            if (random.randint(1,2) == 2):
                newFly = Group(
                Oval(280, 180, 25, 15, fill='black'),
                Oval(273, 172, 15, 10, fill='white', opacity = 50, rotateAngle = 40),
                Oval(280, 172, 15, 10, fill='white', opacity = 50, rotateAngle = 40),
                )
                newFly.centerX = -100 - random.randint(-30, 70)
                newFly.centerY = random.randint(120, 270)
                ecoFlies.add (
                    newFly
                )
        ecoFlies.centerX += 2 + app.ecoFlyCount*0.5
        app.ecoFlyTimer -= 1
        if app.ecoTongueTimer >= 0:
            app.ecoTongueTimer -= 1
            frogTongue.visible = True
        else:
            frogTongue.visible = False
        
        if (app.ecoFlyCount == 2):
            broadcastMessage("| Pay attention to the facts |", "| You will be quizzed at the end |")
            ecoFact1.visible = True
            ecoFact2.visible = False
            ecoFact3.visible = False
            ecoFact4.visible = False
            ecoFact5.visible = False
            ecoFact6.visible = False
            ecoFact7.visible = False
            ecoFact8.visible = False
            ecoFact9.visible = False
            ecoFact10.visible = False
        elif (app.ecoFlyCount == 7):
            ecoFact1.visible = False
            ecoFact2.visible = True
            ecoFact3.visible = False
            ecoFact4.visible = False
            ecoFact5.visible = False
            ecoFact6.visible = False
            ecoFact7.visible = False
            ecoFact8.visible = False
            ecoFact9.visible = False
            ecoFact10.visible = False
        elif (app.ecoFlyCount == 10):
            ecoFact1.visible = False
            ecoFact2.visible = False
            ecoFact3.visible = True
            ecoFact4.visible = False
            ecoFact5.visible = False
            ecoFact6.visible = False
            ecoFact7.visible = False
            ecoFact8.visible = False
            ecoFact9.visible = False
            ecoFact10.visible = False
        elif (app.ecoFlyCount == 13):
            ecoFact1.visible = False
            ecoFact2.visible = False
            ecoFact3.visible = False
            ecoFact4.visible = True
            ecoFact5.visible = False
            ecoFact6.visible = False
            ecoFact7.visible = False
            ecoFact8.visible = False
            ecoFact9.visible = False
            ecoFact10.visible = False
        elif (app.ecoFlyCount == 16):
            ecoFact1.visible = False
            ecoFact2.visible = False
            ecoFact3.visible = False
            ecoFact4.visible = False
            ecoFact5.visible = True
            ecoFact6.visible = False
            ecoFact7.visible = False
            ecoFact8.visible = False
            ecoFact9.visible = False
            ecoFact10.visible = False
        elif (app.ecoFlyCount == 19):
            ecoFact1.visible = False
            ecoFact2.visible = False
            ecoFact3.visible = False
            ecoFact4.visible = False
            ecoFact5.visible = False
            ecoFact6.visible = True
            ecoFact7.visible = False
            ecoFact8.visible = False
            ecoFact9.visible = False
            ecoFact10.visible = False
        elif (app.ecoFlyCount == 23):
            ecoFact1.visible = False
            ecoFact2.visible = False
            ecoFact3.visible = False
            ecoFact4.visible = False
            ecoFact5.visible = False
            ecoFact6.visible = False
            ecoFact7.visible = True
            ecoFact8.visible = False
            ecoFact9.visible = False
            ecoFact10.visible = False
        elif (app.ecoFlyCount == 26):
            ecoFact1.visible = False
            ecoFact2.visible = False
            ecoFact3.visible = False
            ecoFact4.visible = False
            ecoFact5.visible = False
            ecoFact6.visible = False
            ecoFact7.visible = False
            ecoFact8.visible = True
            ecoFact9.visible = False
            ecoFact10.visible = False
        elif (app.ecoFlyCount == 29):
            ecoFact1.visible = False
            ecoFact2.visible = False
            ecoFact3.visible = False
            ecoFact4.visible = False
            ecoFact5.visible = False
            ecoFact6.visible = False
            ecoFact7.visible = False
            ecoFact8.visible = False
            ecoFact9.visible = True    
            ecoFact10.visible = False
        elif (app.ecoFlyCount == 32):
            ecoFact1.visible = False
            ecoFact2.visible = False
            ecoFact3.visible = False
            ecoFact4.visible = False
            ecoFact5.visible = False
            ecoFact6.visible = False
            ecoFact7.visible = False
            ecoFact8.visible = False
            ecoFact9.visible = False    
            ecoFact10.visible = True
        elif (app.ecoFlyCount == 35 or app.ecoFlyCount == 36):
            ecoFact1.visible = False
            ecoFact2.visible = False
            ecoFact3.visible = False
            ecoFact4.visible = False
            ecoFact5.visible = False
            ecoFact6.visible = False
            ecoFact7.visible = False
            ecoFact8.visible = False
            ecoFact9.visible = False    
            ecoFact10.visible = False
            
            ecoHearts.visible = False
            frog.visible = False
            cursor.visible = False
            ecoClouds.visible = False
            ecoFlies.clear()
            if (app.ecosystem == False):
                broadcastMessage('| Drag the answers and fill in the blanks |', '')
                ecosystemQuestions.visible = True
                ecosystemAnswers.visible = True
            else:
                ###
                sleep(2)
                menu.visible = True
                app.background = 'green'
                app.status = 'menu'
                app.ecosystemChallenge = False
                broadcastMessage ('| ECOSYSTEM Badge Earned, Congrats! |', '')
            app.ecoFlyCount = 900
        
        

    
            
### END OF ONSTEP            
            
def onKeyHold (keys):
    if (app.geoChallenge==True):
        geoThermStart.toFront()
        if ('s' in keys):
            geoPipe.y2 += 3
            geoPipe2.centerY += 3
        elif ('w' in keys):
            if (geoPipe.y2 <= 0):
                pass
            else:
                geoPipe.y2 -= 3
                geoPipe2.centerY -= 3
        if ('a' in keys):
            if (geoPipe2.centerX <= 20):
                pass
            else:
                geoPipe.x2 -= 3
                geoPipe2.centerX -= 3
        elif ('d' in keys):
            if (geoPipe2.centerX >= 380):
                pass
            else:
                geoPipe.x2 += 3
                geoPipe2.centerX += 3
    if ((app.solarChallenge==True) and (app.solarFact < 10)):
        if ('d' in keys):
            if (solarCar.right < 300):
                solarCar.centerX += 2
                app.solarThrust += 0.07
        elif ('a' in keys):
            if (solarCar.left > 0):
                solarCar.centerX -= 4
                app.solarThrust -= 0.14
        if ('s' in keys):
            solarCar.rotateAngle = 15
            solarCar.centerY += 1*app.solarThrust
        elif ('w' in keys):
            solarCar.rotateAngle = -15
            solarCar.centerY -= 1*app.solarThrust
    if (app.status == 'ozoneChallenge' and ozonePlayer.visible == True):
        if ('left' in keys and ozonePlayer.left > 0):
            ozonePlayer.centerX -= 5
        if ('right' in keys and ozonePlayer.right < 400):
            ozonePlayer.centerX += 5
            
        
            
def onKeyPress (key):
    if ((app.windChallenge == True) and (key=='space') and (bird.centerY < 400)):
        app.windGravity = True
        if ((app.windThrustTimer==60) and (app.windThrust==True)):
            while app.windThrustTimer > 0:
                app.windThrustTimer -= 1
                bird.centerY -= 1
            while app.windThrustTimer < 60:
                app.windThrustTimer += 1
        if (bird.bottom <= 0 ):
            app.windThrust = False
    if (app.ozoneChallenge == True or app.status == "ozoneChallenge"):
        if (key == "space" and ozoneBullet.visible == False):
            ozoneBullet.centerX = ozonePlayer.centerX
            ozoneBullet.centerY = ozonePlayer.centerY - 40
            ozoneBullet.visible = True
    if (app.devHack == True and app.ecosystemChallenge == True and key == 'k'):
        app.ecoFlyCount = 35
                
def onMouseDrag (mouseX, mouseY):
    if ((app.geoChallenge == True) and (app.geoStage == 6)):
        geoThermStart.toFront()
        if ((distance(geoAnswer1.centerX, geoAnswer1.centerY, mouseX, mouseY) < 50) and (geoAnswer1.visible == True)):
            if ((app.geoDrag == 0) or (app.geoDrag == 1)):
                app.geoDrag = 1
                geoAnswer1.centerX = mouseX
                geoAnswer1.centerY = mouseY
        elif ((distance(geoAnswer2.centerX, geoAnswer2.centerY, mouseX, mouseY) < 50) and (geoAnswer2.visible == True)):
            if ((app.geoDrag == 0) or (app.geoDrag == 2)):
                app.geoDrag = 2
                geoAnswer2.centerX = mouseX
                geoAnswer2.centerY = mouseY
        elif ((distance(geoAnswer3.centerX, geoAnswer3.centerY, mouseX, mouseY) < 50) and (geoAnswer3.visible == True)):
            if ((app.geoDrag == 0) or (app.geoDrag == 3)):
                app.geoDrag = 3    
                geoAnswer3.centerX = mouseX
                geoAnswer3.centerY = mouseY
        elif ((distance(geoAnswer4.centerX, geoAnswer4.centerY, mouseX, mouseY) < 50) and (geoAnswer4.visible == True)):
            if ((app.geoDrag == 0) or (app.geoDrag == 4)):
                app.geoDrag = 4    
                geoAnswer4.centerX = mouseX
                geoAnswer4.centerY = mouseY
        elif ((distance(geoAnswer5.centerX, geoAnswer5.centerY, mouseX, mouseY) < 50) and (geoAnswer5.visible == True)):
            if ((app.geoDrag == 0) or (app.geoDrag == 5)):
                app.geoDrag = 5
                geoAnswer5.centerX = mouseX
                geoAnswer5.centerY = mouseY
        if (app.geoDrag > 0):
            if (app.geoDrag == 1):
                geoAnswer1.centerX = mouseX
                geoAnswer1.centerY = mouseY
            elif (app.geoDrag == 2):
                geoAnswer2.centerX = mouseX
                geoAnswer2.centerY = mouseY
            elif (app.geoDrag == 3):
                geoAnswer3.centerX = mouseX
                geoAnswer3.centerY = mouseY
            elif (app.geoDrag == 4):
                geoAnswer4.centerX = mouseX
                geoAnswer4.centerY = mouseY
            elif (app.geoDrag == 5):
                geoAnswer5.centerX = mouseX
                geoAnswer5.centerY = mouseY
### SOLAR
    if ((app.solarChallenge == True) and (app.solarFact == 10)):
        if ((distance(solarAnswer1.centerX, solarAnswer1.centerY, mouseX, mouseY) < 50) and (solarAnswer1.visible == True)):
            if ((app.solarDrag == 0) or (app.solarDrag == 1)):
                app.solarDrag = 1
                solarAnswer1.centerX = mouseX
                solarAnswer1.centerY = mouseY
        elif ((distance(solarAnswer2.centerX, solarAnswer2.centerY, mouseX, mouseY) < 50) and (solarAnswer2.visible == True)):
            if ((app.solarDrag == 0) or (app.solarDrag == 2)):
                app.solarDrag = 2
                solarAnswer2.centerX = mouseX
                solarAnswer2.centerY = mouseY
        elif ((distance(solarAnswer3.centerX, solarAnswer3.centerY, mouseX, mouseY) < 50) and (solarAnswer3.visible == True)):
            if ((app.solarDrag == 0) or (app.solarDrag == 3)):
                app.solarDrag = 3    
                solarAnswer3.centerX = mouseX
                solarAnswer3.centerY = mouseY
        elif ((distance(solarAnswer4.centerX, solarAnswer4.centerY, mouseX, mouseY) < 50) and (solarAnswer4.visible == True)):
            if ((app.solarDrag == 0) or (app.solarDrag == 4)):
                app.solarDrag = 4    
                solarAnswer4.centerX = mouseX
                solarAnswer4.centerY = mouseY
        elif ((distance(solarAnswer5.centerX, solarAnswer5.centerY, mouseX, mouseY) < 50) and (solarAnswer5.visible == True)):
            if ((app.solarDrag == 0) or (app.solarDrag == 5)):
                app.solarDrag = 5
                solarAnswer5.centerX = mouseX
                solarAnswer5.centerY = mouseY
        if (app.solarDrag > 0):
            if (app.solarDrag == 1):
                solarAnswer1.centerX = mouseX
                solarAnswer1.centerY = mouseY
            elif (app.solarDrag == 2):
                solarAnswer2.centerX = mouseX
                solarAnswer2.centerY = mouseY
            elif (app.solarDrag == 3):
                solarAnswer3.centerX = mouseX
                solarAnswer3.centerY = mouseY
            elif (app.solarDrag == 4):
                solarAnswer4.centerX = mouseX
                solarAnswer4.centerY = mouseY
            elif (app.solarDrag == 5):
                solarAnswer5.centerX = mouseX
                solarAnswer5.centerY = mouseY
### WIND
    if ((app.windChallenge == True) and (windPowerQuestions.visible == True)):
        if ((distance(windAnswer1.centerX, windAnswer1.centerY, mouseX, mouseY) < 50) and (windAnswer1.visible == True)):
            if ((app.windDrag == 0) or (app.windDrag == 1)):
                app.windDrag = 1
                windAnswer1.centerX = mouseX
                windAnswer1.centerY = mouseY
        elif ((distance(windAnswer2.centerX, windAnswer2.centerY, mouseX, mouseY) < 50) and (windAnswer2.visible == True)):
            if ((app.windDrag == 0) or (app.windDrag == 2)):
                app.windDrag = 2
                windAnswer2.centerX = mouseX
                windAnswer2.centerY = mouseY
        elif ((distance(windAnswer3.centerX, windAnswer3.centerY, mouseX, mouseY) < 50) and (windAnswer3.visible == True)):
            if ((app.windDrag == 0) or (app.windDrag == 3)):
                app.windDrag = 3
                windAnswer3.centerX = mouseX
                windAnswer3.centerY = mouseY
        elif ((distance(windAnswer4.centerX, windAnswer4.centerY, mouseX, mouseY) < 50) and (windAnswer4.visible == True)):
            if ((app.windDrag == 0) or (app.windDrag == 4)):
                app.windDrag = 4
                windAnswer4.centerX = mouseX
                windAnswer4.centerY = mouseY
        elif ((distance(windAnswer5.centerX, windAnswer5.centerY, mouseX, mouseY) < 50) and (windAnswer5.visible == True)):
            if ((app.windDrag == 0) or (app.windDrag == 5)):
                app.windDrag = 5
                windAnswer5.centerX = mouseX
                windAnswer5.centerY = mouseY
        if (app.solarDrag > 0):
            if (app.solarDrag == 1):
                windAnswer1.centerX = mouseX
                windAnswer1.centerY = mouseY
            elif (app.solarDrag == 2):
                windAnswer2.centerX = mouseX
                windAnswer2.centerY = mouseY
            elif (app.solarDrag == 3):
                windAnswer3.centerX = mouseX
                windAnswer3.centerY = mouseY
            elif (app.solarDrag == 4):
                windAnswer4.centerX = mouseX
                windAnswer4.centerY = mouseY
            elif (app.solarDrag == 5):
                windAnswer5.centerX = mouseX
                windAnswer5.centerY = mouseY
                
### OZONE
    if ((app.ozoneChallenge == True) and (ozoneLayerQuestions.visible == True)):
        if ((distance(ozoneAnswer1.centerX, ozoneAnswer1.centerY, mouseX, mouseY) < 50) and (ozoneAnswer1.visible == True)):
            if ((app.ozoneDrag == 0) or (app.ozoneDrag == 1)):
                app.ozoneDrag = 1
                ozoneAnswer1.centerX = mouseX
                ozoneAnswer1.centerY = mouseY
        elif ((distance(ozoneAnswer2.centerX, ozoneAnswer2.centerY, mouseX, mouseY) < 50) and (ozoneAnswer2.visible == True)):
            if ((app.ozoneDrag == 0) or (app.ozoneDrag == 2)):
                app.ozoneDrag = 2
                ozoneAnswer2.centerX = mouseX
                ozoneAnswer2.centerY = mouseY
        elif ((distance(ozoneAnswer3.centerX, ozoneAnswer3.centerY, mouseX, mouseY) < 50) and (ozoneAnswer3.visible == True)):
            if ((app.ozoneDrag == 0) or (app.ozoneDrag == 3)):
                app.ozoneDrag = 3
                ozoneAnswer3.centerX = mouseX
                ozoneAnswer3.centerY = mouseY
        elif ((distance(ozoneAnswer4.centerX, ozoneAnswer4.centerY, mouseX, mouseY) < 50) and (ozoneAnswer4.visible == True)):
            if ((app.ozoneDrag == 0) or (app.ozoneDrag == 4)):
                app.ozoneDrag = 4
                ozoneAnswer4.centerX = mouseX
                ozoneAnswer4.centerY = mouseY
        elif ((distance(ozoneAnswer5.centerX, ozoneAnswer5.centerY, mouseX, mouseY) < 50) and (ozoneAnswer5.visible == True)):
            if ((app.ozoneDrag == 0) or (app.ozoneDrag == 5)):
                app.ozoneDrag = 5
                ozoneAnswer5.centerX = mouseX
                ozoneAnswer5.centerY = mouseY
        if (app.ozoneDrag > 0):
            if (app.ozoneDrag == 1):
                ozoneAnswer1.centerX = mouseX
                ozoneAnswer1.centerY = mouseY
            elif (app.ozoneDrag == 2):
                ozoneAnswer2.centerX = mouseX
                ozoneAnswer2.centerY = mouseY
            elif (app.ozoneDrag == 3):
                ozoneAnswer3.centerX = mouseX
                ozoneAnswer3.centerY = mouseY
            elif (app.ozoneDrag == 4):
                ozoneAnswer4.centerX = mouseX
                ozoneAnswer4.centerY = mouseY
            elif (app.ozoneDrag == 5):
                ozoneAnswer5.centerX = mouseX
                ozoneAnswer5.centerY = mouseY
    ### ECOSYSTEM
    if ((app.ecosystemChallenge == True) and (ecosystemQuestions.visible == True)):
        if ((distance(ecoAnswer1.centerX, ecoAnswer1.centerY, mouseX, mouseY) < 50) and (ecoAnswer1.visible == True)):
            if ((app.ecosystemDrag == 0) or (app.ecosystemDrag == 1)):
                app.ecosystemDrag = 1
                ecoAnswer1.centerX = mouseX
                ecoAnswer1.centerY = mouseY
        elif ((distance(ecoAnswer2.centerX, ecoAnswer2.centerY, mouseX, mouseY) < 50) and (ecoAnswer2.visible == True)):
            if ((app.ecosystemDrag == 0) or (app.ecosystemDrag == 2)):
                app.ecosystemDrag = 2
                ecoAnswer2.centerX = mouseX
                ecoAnswer2.centerY = mouseY
        elif ((distance(ecoAnswer3.centerX, ecoAnswer3.centerY, mouseX, mouseY) < 50) and (ecoAnswer3.visible == True)):
            if ((app.ecosystemDrag == 0) or (app.ecosystemDrag == 3)):
                app.ecosystemDrag = 3
                ecoAnswer3.centerX = mouseX
                ecoAnswer3.centerY = mouseY
        elif ((distance(ecoAnswer4.centerX, ecoAnswer4.centerY, mouseX, mouseY) < 50) and (ecoAnswer4.visible == True)):
            if ((app.ecosystemDrag == 0) or (app.ecosystemDrag == 4)):
                app.ecosystemDrag = 4
                ecoAnswer4.centerX = mouseX
                ecoAnswer4.centerY = mouseY
        elif ((distance(ecoAnswer5.centerX, ecoAnswer5.centerY, mouseX, mouseY) < 50) and (ecoAnswer5.visible == True)):
            if ((app.ecosystemDrag == 0) or (app.ecosystemDrag == 5)):
                app.ecosystemDrag = 5
                ecoAnswer5.centerX = mouseX
                ecoAnswer5.centerY = mouseY
        if (app.ecosystemDrag > 0):
            if (app.ecosystemDrag == 1):
                ecoAnswer1.centerX = mouseX
                ecoAnswer1.centerY = mouseY
            elif (app.ecosystemDrag == 2):
                ecoAnswer2.centerX = mouseX
                ecoAnswer2.centerY = mouseY
            elif (app.ecosystemDrag == 3):
                ecoAnswer3.centerX = mouseX
                ecoAnswer3.centerY = mouseY
            elif (app.ecosystemDrag == 4):
                ecoAnswer4.centerX = mouseX
                ecoAnswer4.centerY = mouseY
            elif (app.ecosystemDrag == 5):
                ecoAnswer5.centerX = mouseX
                ecoAnswer5.centerY = mouseY


    if (app.devHack == True):
        if ((distance (mouseX, mouseY, geoPipe2.centerX, geoPipe2.centerY) <= 80) and (app.geoChallenge == True)):
            geoPipe2.centerX = mouseX
            geoPipe.x2 = mouseX
            geoPipe2.centerY = mouseY
            geoPipe.y2 = mouseY
            
def onMouseRelease (mouseX, mouseY):
    if ((geoQuestion1.hitsShape(geoAnswer1)) and (geoAnswer1.visible == True)):
            geoAnswer1.visible = False
            geoQuestion1.visible = False
            app.geoScore += 1
    if ((geoQuestion2.hitsShape(geoAnswer2)) and (geoAnswer2.visible == True)):
            geoAnswer2.visible = False
            geoQuestion2.visible = False
            app.geoScore += 1
    if ((geoQuestion3.hitsShape(geoAnswer3)) and (geoAnswer3.visible == True)):
            geoAnswer3.visible = False
            geoQuestion3.visible = False
            app.geoScore += 1
    if ((geoQuestion4.hitsShape(geoAnswer4)) and (geoAnswer4.visible == True)):
            geoAnswer4.visible = False
            geoQuestion4.visible = False
            app.geoScore += 1
    if ((geoQuestion5.hitsShape(geoAnswer5)) and (geoAnswer5.visible == True)):
                geoAnswer5.visible = False
                geoQuestion5.visible = False
                app.geoScore += 1
    if ((app.geoScore == 5) and (app.status == 'geoChallenge') and (app.geoStage == 6)):
        menu.visible = True
        geoThermQuestions.visible = False
        geoThermAnswers.visible = False
        geoThermPart4.visible = False
        geoPipe.visible = False
        geoPipe2.visible = False
        app.background = 'green'
        geoThermBadgePart.fill = 'white'
        geoThermBadgePart.border = 'gainsboro'
        geoThermLabel.fill='white'
        geoThermPart2.fill='orange'
        geoThermPart3.fill='yellow'
        app.geoChallenge = False
        geoThermStart.visible = False
        broadcastMessage ('| GEOTHERMAL Badge Earned, Congrats! |', '')
        app.status = 'menu'
        app.geoChallenge = False
        app.geoTherm  = True
### SOLAR
    if ((solarQuestion1.hitsShape(solarAnswer1)) and (solarAnswer1.visible == True)):
            solarAnswer1.visible = False
            solarQuestion1.visible = False
            app.solarScore += 1
    if ((solarQuestion2.hitsShape(solarAnswer2)) and (solarAnswer2.visible == True)):
            solarAnswer2.visible = False
            solarQuestion2.visible = False
            app.solarScore += 1
    if ((solarQuestion3.hitsShape(solarAnswer3)) and (solarAnswer3.visible == True)):
            solarAnswer3.visible = False
            solarQuestion3.visible = False
            app.solarScore += 1
    if ((solarQuestion4.hitsShape(solarAnswer4)) and (solarAnswer4.visible == True)):
            solarAnswer4.visible = False
            solarQuestion4.visible = False
            app.solarScore += 1
    if ((solarQuestion5.hitsShape(solarAnswer5)) and (solarAnswer5.visible == True)):
                solarAnswer5.visible = False
                solarQuestion5.visible = False
                app.solarScore += 1
    if ((app.solarScore == 5) and (app.status == 'solarChallenge') and (app.solarFact == 10)):
        menu.visible = True
        solarPowerQuestions.visible = False
        solarPowerAnswers.visible = False
        solarPowerPart4.visible = False
        app.background = 'green'
        solarPowerBadgePart.fill = 'white'
        solarPowerBadgePart.border = 'gainsboro'
        solarPowerLabel.fill='white'
        solarPowerPart2.fill='orange'
        solarPowerPart3.fill='yellow'
        app.solarChallenge = False
        broadcastMessage ('| SOLAR Badge Earned, Congrats! |', '')
        app.status = 'menu'
        app.solarPower  = True
    ### WIND    
    if ((windQuestion1.hitsShape(windAnswer1)) and (windAnswer1.visible == True)):
            windAnswer1.visible = False
            windQuestion1.visible = False
            app.windScore += 1
    if ((windQuestion2.hitsShape(windAnswer2)) and (windAnswer2.visible == True)):
            windAnswer2.visible = False
            windQuestion2.visible = False
            app.windScore += 1
    if ((windQuestion3.hitsShape(windAnswer3)) and (windAnswer3.visible == True)):
            windAnswer3.visible = False
            windQuestion3.visible = False
            app.windScore += 1
    if ((windQuestion4.hitsShape(windAnswer4)) and (windAnswer4.visible == True)):
            windAnswer4.visible = False
            windQuestion4.visible = False
            app.windScore += 1
    if ((windQuestion5.hitsShape(windAnswer5)) and (windAnswer5.visible == True)):
            windAnswer5.visible = False
            windQuestion5.visible = False
            app.windScore += 1
    if ((app.windScore == 5) and (app.status == 'windChallenge') and (windPowerQuestions.visible == True)):
        menu.visible = True
        windPowerQuestions.visible = False
        windPowerAnswers.visible = False
        windPowerPart4.visible = False
        app.background = 'green'
        windPowerBadgePart.fill = 'white'
        windPowerBadgePart.border = 'gainsboro'
        windPowerLabel.fill='white'
        app.windChallenge = False
        broadcastMessage ('| WIND Badge Earned, Congrats! |', '')
        app.status = 'menu'
        app.windPower  = True
        
    ### OZONE
    
    if ((ozoneQuestion1.hitsShape(ozoneAnswer1)) and (ozoneAnswer1.visible == True)):
            ozoneAnswer1.visible = False
            ozoneQuestion1.visible = False
            app.ozoneScore += 1
    if ((ozoneQuestion2.hitsShape(ozoneAnswer2)) and (ozoneAnswer2.visible == True)):
            ozoneAnswer2.visible = False
            ozoneQuestion2.visible = False
            app.ozoneScore += 1
    if ((ozoneQuestion3.hitsShape(ozoneAnswer3)) and (ozoneAnswer3.visible == True)):
            ozoneAnswer3.visible = False
            ozoneQuestion3.visible = False
            app.ozoneScore += 1
    if ((ozoneQuestion4.hitsShape(ozoneAnswer4)) and (ozoneAnswer4.visible == True)):
            ozoneAnswer4.visible = False
            ozoneQuestion4.visible = False
            app.ozoneScore += 1
    if ((ozoneQuestion5.hitsShape(ozoneAnswer5)) and (ozoneAnswer5.visible == True)):
            ozoneAnswer5.visible = False
            ozoneQuestion5.visible = False
            app.ozoneScore += 1
    
    ### ECOSYSTEM
    if  (app.ecoFlyCount >= 35):
        if ((ecoQuestion1.hitsShape(ecoAnswer1)) and (ecoAnswer1.visible == True)):
                ecoAnswer1.visible = False
                ecoQuestion1.visible = False
                app.ecosystemScore += 1
        if ((ecoQuestion2.hitsShape(ecoAnswer2)) and (ecoAnswer2.visible == True)):
                ecoAnswer2.visible = False
                ecoQuestion2.visible = False
                app.ecosystemScore += 1
        if ((ecoQuestion3.hitsShape(ecoAnswer3)) and (ecoAnswer3.visible == True)):
                ecoAnswer3.visible = False
                ecoQuestion3.visible = False
                app.ecosystemScore += 1
        if ((ecoQuestion4.hitsShape(ecoAnswer4)) and (ecoAnswer4.visible == True)):
                ecoAnswer4.visible = False
                ecoQuestion4.visible = False
                app.ecosystemScore += 1
        if ((ecoQuestion5.hitsShape(ecoAnswer5)) and (ecoAnswer5.visible == True)):
                ecoAnswer5.visible = False
                ecoQuestion5.visible = False
                app.ecosystemScore += 1
        
        if ((app.ecosystemScore == 5) and (app.status == 'ecosystemChallenge') and (ecosystemQuestions.visible == True)):
            menu.visible = True
            app.background = 'green'
            ecosystemPart4.visible = False
            ecosystemPart3.fill = rgb(71, 134, 71)
            #ecosystemBadge.remove(ecosystemPart2)
            app.status = 'menu'
            app.ecosystem = True
            app.ecosystemChallenge = False
            
            ecosystemPart2 = Group (
                Oval (200, 300, 60, 50, fill=rgb(36, 182, 36)),
                Oval (175, 280, 20, 20, fill=rgb(36, 182, 36)),
                Oval (225, 280, 20, 20, fill=rgb(36, 182, 36)),
                Circle (175, 280, 6, fill='white'),
                Circle (225, 280, 6, fill='white'),
                Circle (175, 280, 4, fill='black'),
                Circle (225, 280, 4, fill='black'),
                )
            
            #ecosystemPart3 = Arc (200, 305, 20, 20, 90, 180, fill=rgb(1,61,1))
            ecosystemLabel.fill = 'white'
            ecosystemBadge.add(ecosystemPart2)
            ecosystemBadge.add(ecosystemPart3)
            ecosystemBadgePart.fill = 'white'
            ecosystemBadgePart.border = 'gainsboro'
            ecosystemPart3.toFront()
            broadcastMessage ('| ECOSYSTEM Badge Earned, Congrats! |', '')
        
        
    
    app.geoDrag = 0
    app.solarDrag = 0
    app.windDrag = 0
    app.ozoneDrag = 0
    app.ecosystemDrag = 0
    
def onKeyRelease (key):
    solarCar.rotateAngle  = 0
            
def onMouseMove(mouseX, mouseY):
    if (goButton.contains(mouseX, mouseY)):
        goLabel.size = 21
    else:
        goLabel.size = 18
    if (loginButton.contains(mouseX, mouseY)):
        loginLabel.size = 21
    else:
        loginLabel.size = 18
    if (app.status == 'ecosystemChallenge'):
        frogEye.centerX = 200 - ((200-mouseX)/100)
        frogEye.centerY = 338 - ((200-mouseY)/100)
    if (app.status == 'menu'):
        if (geoThermBadge.contains(mouseX, mouseY)):
            geoThermLabel.size=15
        else:
            geoThermLabel.size=12
        if (solarPowerBadge.contains(mouseX, mouseY)):
            solarPowerLabel.size=15
        else:
            solarPowerLabel.size=12
        if (windPowerBadge.contains(mouseX, mouseY)):
            windPowerLabel.size=15
        else:
            windPowerLabel.size=12
        if (ozoneBadge.contains(mouseX, mouseY)):
            ozoneLabel.size=15
        else:
            ozoneLabel.size=12
        if (ecosystemBadge.contains(mouseX, mouseY)):
            ecosystemLabel.size=15
        else:
            ecosystemLabel.size=12
        if (trophyBadge.contains(mouseX, mouseY)):
            trophyLabel.size=15
        else:
            trophyLabel.size=12
    if (app.ecosystemChallenge == True):
        if (cursor.visible == True):
            cursor.centerX = mouseX
            cursor.centerY = mouseY
def onMousePress (mouseX, mouseY):
    if ((goButton.contains(mouseX, mouseY)) and (goButton.visible == True)):
        loading()
        introScreen.visible = False
        menu.visible = True
        app.status = 'menu'
    if ((app.status == 'menu') and (saveButton.contains(mouseX, mouseY))):
        generatePassword()
    if ((loginButton.contains(mouseX, mouseY)) and (loginButton.visible == True)):
        app.password = str(app.getTextInput('Enter password:'))
        login(app.password)
        loading()
        introScreen.visible = False
        menu.visible = True
        app.status = 'menu'
        if (app.solarPower == True):
            solarPowerPart4.visible = False
        if (app.windPower == True):
            windPowerPart4.visible = False
    elif ((app.status == 'menu') and (geoThermBadge.contains(mouseX, mouseY)) and (geoThermBadge.visible == True) and (loadingTrees.top>=0)):
        app.geoStage = 0
        menu.visible = False
        geoThermChallenge()
    elif ((app.status == 'menu') and (solarPowerBadge.contains(mouseX, mouseY)) and (solarPowerBadge.visible == True) and (loadingTrees.top>=0)):
        app.solarFact=1
        solarCar.centerY = 200
        solarOrb.centerX = 200
        solarOrb.centerY = 200
        app.solarBattery = 7
        solarTrack1.centerX = 210
        solarLine1.centerX = 400
        solarCar.centerX = 40
        app.solarThrust = 0
        solarCourse1.centerX = 1148
        solarCourse2.centerX = 1148
        solarCourse3.centerX = 998
        menu.visible = False
        app.solarFact = 1
        app.solarBattery = 7
        if (solarFact1.visible == True):
            solarFact1.visible = False
        if (solarFact2.visible == True):
            solarFact2.visible = False
        if (solarFact3.visible == True):
            solarFact3.visible = False
        if (solarFact4.visible == True):
            solarFact4.visible = False
        if (solarFact5.visible == True):
            solarFact5.visible = False
        if (solarFact6.visible == True):
            solarFact6.visible = False
        if (solarFact7.visible == True):
            solarFact7.visible = False
        if (solarFact8.visible == True):
            solarFact8.visible = False
        if (solarFact9.visible == True):
            solarFact9.visible = False
        solarFact1.visible = True
        solarTrack1.centerX = 210
        solarLine1.centerX = 400
        solarCar.centerX = 40
        app.solarThrust = 0
        solarCourse1.centerX = 1148
        solarCourse2.centerX = 1148
        solarCourse3.centerX = 958
        solarCar.centerY = 200
        solarCourse1.visible = True
        solarCourse2.visible = False
        solarCourse3.visible = False
        solarOrbNext()
        solarOrb.toFront()
        solarPowerChallenge()
    elif ((app.status == 'menu') and (windPowerBadge.contains(mouseX, mouseY)) and (windPowerBadge.visible == True) and (loadingTrees.top>=0)):
        windPowerChallenge()
        menu.visible = False
    elif ((app.status == 'menu') and (ozoneBadge.contains(mouseX, mouseY)) and (ozoneBadge.visible == True) and (loadingTrees.top>=0)):
        ozoneLayerChallenge()
    elif ((app.status == 'menu') and (ecosystemBadge.contains(mouseX, mouseY)) and (ecosystemBadge.visible == True) and (loadingTrees.top>=0)):
        ecosystemChallenge()
    if (passwordBox.contains(mouseX, mouseY)):
        passwordBox.visible = False
    
    elif ((app.status == 'menu') and (trophyBadge.contains(mouseX, mouseY)) and (trophyBadge.visible == True) and (loadingTrees.top>=0)):
        if ((app.geoTherm == True and app.solarPower == True and app.windPower == True and app.ozoneLayer == True and app.ecosystem == True) or app.devHack==True):
            menu.visible = False
            app.background = 'white'
            app.status = 'trophy'
            if (app.name == 0):
                app.name = app.getTextInput("Please enter your full name for your certificate:")
                certifyLabel.value = app.name
            certify.visible = True
            trophyLabel.value = "CERTIFICATE"
        else:
            broadcastMessage("{ Badge LOCKED }", "Complete all the other badges to unlock!")
    elif (app.status == 'trophy'):
        app.status = 'menu'
        app.background = 'green'
        menu.visible = True
        certify.visible = False
    
    if (app.ecosystemChallenge == True):
        if (ecoFlies.hitsShape(cursor)):
            app.ecoTongueTimer = 10
            frogTongue.x2 = cursor.centerX
            frogTongue.y2 = cursor.centerY
            ecoClouds.toBack()
            #frogTongue.toBack()
            cursor.toFront()
            for i in ecoFlies:
                if i.hitsShape(cursor) == True:
                    ecoFlies.remove(i)
                    app.ecoFlyCount += 1
    
    if (app.devHack == True and app.ozoneChallenge == True):
        if (len(ozoneInvaders.children) > 0):
            ozoneInvaders.clear()
    #        ozoneInvaders.delete(ozoneInvaders.hitTest(mouseX, mouseY))
    
def resetOzone():
    sleep(3)
    if (ozoneInvaders.bottom >= 350):
        broadcastMessage("Oops! You got overrun! Be careful!", "SPACE to shoot and Left/Right keys to move")
        ozonePlayer.centerX = 200
    ozoneInvaders.clear()
    
    if (app.ozoneFact == 0):
        ozoneInvaders.add(
                Circle (50, 130, 10, fill='red'),
                Circle (80, 130, 10, fill='red'),
                Circle (110, 130, 10, fill='red'),
                Circle (140, 130, 10, fill='red'),
                Circle (170, 130, 10, fill='red'),
                Circle (200, 130, 10, fill='red'),
                Circle (50, 160, 10, fill='red'),
                Circle (80, 160, 10, fill='red'),
                Circle (110, 160, 10, fill='red'),
                Circle (140, 160, 10, fill='red'),
                Circle (170, 160, 10, fill='red'),
                Circle (200, 160, 10, fill='red'),
            )
    elif (app.ozoneFact ==1):
        ozoneInvaders.add(
                Circle (50, 130, 10, fill='red'),
                Circle (80, 130, 10, fill='red'),
                Circle (110, 130, 10, fill='red'),
                Circle (140, 130, 10, fill='red'),
                Circle (170, 130, 10, fill='red'),
                Circle (200, 130, 10, fill='red'),
                Circle (230, 130, 10, fill='red'),
                Circle (260, 130, 10, fill='red'),
                Circle (290, 130, 10, fill='red'),
                Circle (50, 160, 10, fill='red'),
                Circle (80, 160, 10, fill='red'),
                Circle (110, 160, 10, fill='red'),
                Circle (140, 160, 10, fill='red'),
                Circle (170, 160, 10, fill='red'),
                Circle (200, 160, 10, fill='red'),
                Circle (230, 160, 10, fill='red'),
                Circle (260, 160, 10, fill='red'),
                Circle (290, 160, 10, fill='red'),
            )
        broadcastMessage("| Pay attention to the facts |", "| You will be quizzed at the end |")
    elif (app.ozoneFact ==2):
        ozoneInvaders.add (
                Circle (50, 130, 10, fill='red'),
                Circle (80, 130, 10, fill='red'),
                Circle (110, 130, 10, fill='red'),
                Circle (140, 130, 10, fill='red'),
                Circle (170, 130, 10, fill='red'),
                Circle (200, 130, 10, fill='red'),
                Circle (230, 130, 10, fill='red'),
                Circle (260, 130, 10, fill='red'),
                Circle (290, 130, 10, fill='red'),
                Circle (320, 130, 10, fill='red'),
                Circle (50, 160, 10, fill='red'),
                Circle (80, 160, 10, fill='red'),
                Circle (110, 160, 10, fill='red'),
                Circle (140, 160, 10, fill='red'),
                Circle (170, 160, 10, fill='red'),
                Circle (200, 160, 10, fill='red'),
                Circle (230, 160, 10, fill='red'),
                Circle (260, 160, 10, fill='red'),
                Circle (290, 160, 10, fill='red'),
                Circle (320, 160, 10, fill='red'),
                Circle (50, 190, 10, fill='red'),
                Circle (80, 190, 10, fill='red'),
                Circle (110, 190, 10, fill='red'),
                Circle (140, 190, 10, fill='red'),
                Circle (170, 190, 10, fill='red'),
                Circle (200, 190, 10, fill='red'),
                Circle (230, 190, 10, fill='red'),
                Circle (260, 190, 10, fill='red'),
                Circle (290, 190, 10, fill='red'),
                Circle (320, 190, 10, fill='red'),
            )
    elif (app.ozoneFact == 3):
        ozoneInvaders.add (
                Circle (50, 130, 10, fill='red'),
                Circle (80, 130, 10, fill='red'),
                Circle (110, 130, 10, fill='red'),
                Circle (140, 130, 10, fill='red'),
                Circle (170, 130, 10, fill='red'),
                Circle (200, 130, 10, fill='red'),
                Circle (230, 130, 10, fill='red'),
                Circle (260, 130, 10, fill='red'),
                Circle (290, 130, 10, fill='red'),
                #Circle (320, 130, 10, fill='red'),
                Circle (50, 160, 10, fill='red'),
                Circle (80, 160, 10, fill='red'),
                Circle (110, 160, 10, fill='red'),
                Circle (140, 160, 10, fill='red'),
                Circle (170, 160, 10, fill='red'),
                Circle (200, 160, 10, fill='red'),
                Circle (230, 160, 10, fill='red'),
                Circle (260, 160, 10, fill='red'),
                Circle (290, 160, 10, fill='red'),
                #Circle (320, 160, 10, fill='red'),
                Circle (50, 190, 10, fill='red'),
                Circle (80, 190, 10, fill='red'),
                Circle (110, 190, 10, fill='red'),
                Circle (140, 190, 10, fill='red'),
                Circle (170, 190, 10, fill='red'),
                Circle (200, 190, 10, fill='red'),
                Circle (230, 190, 10, fill='red'),
                Circle (260, 190, 10, fill='red'),
                Circle (290, 190, 10, fill='red'),
                #Circle (320, 190, 10, fill='red'),
                
                Circle (50, 220, 10, fill='red'),
                Circle (50, 250, 10, fill='red'),
                Circle (110, 220, 10, fill='red'),
                Circle (110, 250, 10, fill='red'),
                Circle (170, 220, 10, fill='red'),
                Circle (170, 250, 10, fill='red'),
                Circle (230, 220, 10, fill='red'),
                Circle (230, 250, 10, fill='red'),
                Circle (290, 220, 10, fill='red'),
                Circle (290, 250, 10, fill='red'),
            )
    elif (app.ozoneFact == 4):
        ozoneInvaders.add (
                Circle (50, 130, 10, fill='red'),
                Circle (80, 130, 10, fill='red'),
                Circle (110, 130, 10, fill='red'),
                Circle (140, 130, 10, fill='red'),
                Circle (170, 130, 10, fill='red'),
                Circle (200, 130, 10, fill='red'),
                Circle (230, 130, 10, fill='red'),
                Circle (260, 130, 10, fill='red'),
                Circle (290, 130, 10, fill='red'),
                #Circle (320, 130, 10, fill='red'),
                Circle (50, 160, 10, fill='red'),
                Circle (80, 160, 10, fill='red'),
                Circle (110, 160, 10, fill='red'),
                Circle (140, 160, 10, fill='red'),
                Circle (170, 160, 10, fill='red'),
                Circle (200, 160, 10, fill='red'),
                Circle (230, 160, 10, fill='red'),
                Circle (260, 160, 10, fill='red'),
                Circle (290, 160, 10, fill='red'),
                #Circle (320, 160, 10, fill='red'),
                Circle (50, 190, 10, fill='red'),
                Circle (80, 190, 10, fill='red'),
                Circle (110, 190, 10, fill='red'),
                Circle (140, 190, 10, fill='red'),
                Circle (170, 190, 10, fill='red'),
                Circle (200, 190, 10, fill='red'),
                Circle (230, 190, 10, fill='red'),
                Circle (260, 190, 10, fill='red'),
                Circle (290, 190, 10, fill='red'),
                #Circle (320, 190, 10, fill='red'),
                Circle (80, 220, 10, fill='red'),
                Circle (140, 220, 10, fill='red'),
                Circle (200, 220, 10, fill='red'),
                Circle (260, 220, 10, fill='red'),
                
                Circle (50, 220, 10, fill='red'),
                Circle (50, 250, 10, fill='red'),
                Circle (50, 280, 10, fill='red'),
                Circle (110, 220, 10, fill='red'),
                Circle (110, 250, 10, fill='red'),
                Circle (170, 220, 10, fill='red'),
                Circle (170, 250, 10, fill='red'),
                Circle (230, 220, 10, fill='red'),
                Circle (230, 250, 10, fill='red'),
                Circle (290, 220, 10, fill='red'),
                Circle (290, 250, 10, fill='red'),
                Circle (290, 280, 10, fill='red'),
            )
    elif (app.ozoneFact == 5):
        ozoneInvaders.add (
                Circle (50, 130, 10, fill='red'),
                Circle (80, 130, 10, fill='red'),
                Circle (110, 130, 10, fill='red'),
                Circle (140, 130, 10, fill='red'),
                Circle (170, 130, 10, fill='red'),
                Circle (200, 130, 10, fill='red'),
                Circle (230, 130, 10, fill='red'),
                Circle (260, 130, 10, fill='red'),
                Circle (290, 130, 10, fill='red'),
                Circle (320, 130, 10, fill='red'),
                Circle (50, 160, 10, fill='red'),
                Circle (80, 160, 10, fill='red'),
                Circle (110, 160, 10, fill='red'),
                Circle (140, 160, 10, fill='red'),
                Circle (170, 160, 10, fill='red'),
                Circle (200, 160, 10, fill='red'),
                Circle (230, 160, 10, fill='red'),
                Circle (260, 160, 10, fill='red'),
                Circle (290, 160, 10, fill='red'),
                Circle (320, 160, 10, fill='red'),
                Circle (50, 190, 10, fill='red'),
                Circle (80, 190, 10, fill='red'),
                Circle (110, 190, 10, fill='red'),
                Circle (140, 190, 10, fill='red'),
                Circle (170, 190, 10, fill='red'),
                Circle (200, 190, 10, fill='red'),
                Circle (230, 190, 10, fill='red'),
                Circle (260, 190, 10, fill='red'),
                Circle (290, 190, 10, fill='red'),
                Circle (320, 190, 10, fill='red'),
                Circle (80, 220, 10, fill='red'),
                Circle (140, 220, 10, fill='red'),
                Circle (200, 220, 10, fill='red'),
                Circle (260, 220, 10, fill='red'),
                Circle (320, 220, 10, fill='red'),
                Circle (320, 250, 10, fill='red'),
                Circle (320, 280, 10, fill='red'),
                Circle (80, 250, 10, fill='red'),
                Circle (80, 280, 10, fill='red'),
                Circle (140, 250, 10, fill='red'),
                Circle (200, 250, 10, fill='red'),
                Circle (260, 250, 10, fill='red'),
                
                Circle (50, 220, 10, fill='red'),
                Circle (50, 250, 10, fill='red'),
                Circle (50, 280, 10, fill='red'),
                Circle (110, 220, 10, fill='red'),
                Circle (110, 250, 10, fill='red'),
                Circle (170, 220, 10, fill='red'),
                Circle (170, 250, 10, fill='red'),
                Circle (230, 220, 10, fill='red'),
                Circle (230, 250, 10, fill='red'),
                Circle (290, 220, 10, fill='red'),
                Circle (290, 250, 10, fill='red'),
                Circle (290, 280, 10, fill='red'),
            )
    elif (app.ozoneFact == 6):
        ozoneInvaders.add (
                Circle (50, 130, 10, fill='red'),
                Circle (80, 130, 10, fill='red'),
                Circle (110, 130, 10, fill='red'),
                Circle (140, 130, 10, fill='red'),
                Circle (170, 130, 10, fill='red'),
                Circle (200, 130, 10, fill='red'),
                Circle (230, 130, 10, fill='red'),
                Circle (260, 130, 10, fill='red'),
                Circle (290, 130, 10, fill='red'),
                Circle (320, 130, 10, fill='red'),
                Circle (50, 160, 10, fill='red'),
                Circle (80, 160, 10, fill='red'),
                Circle (110, 160, 10, fill='red'),
                Circle (140, 160, 10, fill='red'),
                Circle (170, 160, 10, fill='red'),
                Circle (200, 160, 10, fill='red'),
                Circle (230, 160, 10, fill='red'),
                Circle (260, 160, 10, fill='red'),
                Circle (290, 160, 10, fill='red'),
                Circle (320, 160, 10, fill='red'),
                Circle (50, 190, 10, fill='red'),
                Circle (80, 190, 10, fill='red'),
                Circle (110, 190, 10, fill='red'),
                Circle (140, 190, 10, fill='red'),
                Circle (170, 190, 10, fill='red'),
                Circle (200, 190, 10, fill='red'),
                Circle (230, 190, 10, fill='red'),
                Circle (260, 190, 10, fill='red'),
                Circle (290, 190, 10, fill='red'),
                Circle (320, 190, 10, fill='red'),
                Circle (80, 220, 10, fill='red'),
                Circle (140, 220, 10, fill='red'),
                Circle (200, 220, 10, fill='red'),
                Circle (260, 220, 10, fill='red'),
                Circle (320, 220, 10, fill='red'),
                Circle (320, 250, 10, fill='red'),
                Circle (320, 280, 10, fill='red'),
                Circle (80, 250, 10, fill='red'),
                Circle (80, 280, 10, fill='red'),
                Circle (140, 250, 10, fill='red'),
                Circle (200, 250, 10, fill='red'),
                Circle (260, 250, 10, fill='red'),
                
                Circle (50, 220, 10, fill='red'),
                Circle (50, 250, 10, fill='red'),
                Circle (50, 280, 10, fill='red'),
                Circle (110, 220, 10, fill='red'),
                Circle (110, 250, 10, fill='red'),
                Circle (170, 220, 10, fill='red'),
                Circle (170, 250, 10, fill='red'),
                Circle (230, 220, 10, fill='red'),
                Circle (230, 250, 10, fill='red'),
                Circle (290, 220, 10, fill='red'),
                Circle (290, 250, 10, fill='red'),
                Circle (290, 280, 10, fill='red'),
                
                Circle (170, 280, 10, fill='red'),
                Circle (200, 280, 10, fill='red'),
            )
    elif (app.ozoneFact == 7):
        ozoneInvaders.add (
                Circle (50, 130, 10, fill='red'),
                Circle (80, 130, 10, fill='red'),
                Circle (110, 130, 10, fill='red'),
                Circle (140, 130, 10, fill='red'),
                Circle (170, 130, 10, fill='red'),
                Circle (200, 130, 10, fill='red'),
                Circle (230, 130, 10, fill='red'),
                Circle (260, 130, 10, fill='red'),
                Circle (290, 130, 10, fill='red'),
                Circle (320, 130, 10, fill='red'),
                Circle (50, 160, 10, fill='red'),
                Circle (80, 160, 10, fill='red'),
                Circle (110, 160, 10, fill='red'),
                Circle (140, 160, 10, fill='red'),
                Circle (170, 160, 10, fill='red'),
                Circle (200, 160, 10, fill='red'),
                Circle (230, 160, 10, fill='red'),
                Circle (260, 160, 10, fill='red'),
                Circle (290, 160, 10, fill='red'),
                Circle (320, 160, 10, fill='red'),
                Circle (50, 190, 10, fill='red'),
                Circle (80, 190, 10, fill='red'),
                Circle (110, 190, 10, fill='red'),
                Circle (140, 190, 10, fill='red'),
                Circle (170, 190, 10, fill='red'),
                Circle (200, 190, 10, fill='red'),
                Circle (230, 190, 10, fill='red'),
                Circle (260, 190, 10, fill='red'),
                Circle (290, 190, 10, fill='red'),
                Circle (320, 190, 10, fill='red'),
                Circle (80, 220, 10, fill='red'),
                Circle (140, 220, 10, fill='red'),
                Circle (200, 220, 10, fill='red'),
                Circle (260, 220, 10, fill='red'),
                Circle (320, 220, 10, fill='red'),
                Circle (320, 250, 10, fill='red'),
                #Circle (320, 280, 10, fill='red'),
                Circle (80, 250, 10, fill='red'),
                #Circle (80, 280, 10, fill='red'),
                Circle (140, 250, 10, fill='red'),
                Circle (200, 250, 10, fill='red'),
                Circle (260, 250, 10, fill='red'),
                
                Circle (50, 220, 10, fill='red'),
                Circle (50, 250, 10, fill='red'),
                #Circle (50, 280, 10, fill='red'),
                Circle (110, 220, 10, fill='red'),
                Circle (110, 250, 10, fill='red'),
                Circle (170, 220, 10, fill='red'),
                Circle (170, 250, 10, fill='red'),
                Circle (230, 220, 10, fill='red'),
                Circle (230, 250, 10, fill='red'),
                Circle (290, 220, 10, fill='red'),
                Circle (290, 250, 10, fill='red'),
                #Circle (290, 280, 10, fill='red'),
                
                #Circle (170, 280, 10, fill='red'),
                #Circle (200, 280, 10, fill='red'),
                
                #Circle (110, 280, 10, fill='red'),
                #Circle (140, 280, 10, fill='red'),
                #Circle (230, 280, 10, fill='red'),
                #Circle (260, 280, 10, fill='red'),
                
                Circle (350, 130, 10, fill='red'),
                Circle (350, 160, 10, fill='red'),
                Circle (350, 190, 10, fill='red'),
                Circle (350, 220, 10, fill='red'),
                Circle (350, 250, 10, fill='red'),
                #Circle (350, 280, 10, fill='red'),
                #Circle (350, 310, 10, fill='red'),
                #Circle (50, 310, 10, fill='red'),
            )
    elif (app.ozoneFact == 8):
        ozoneEarth.visible = False
        ozonePlayer.visible = False
        ozoneInvaders.visible = False
        ozoneFact7.visible = False
        if (app.ozoneLayer == False):
            ozoneLayerQuestions.visible = True
            ozoneLayerAnswers.visible = True
            broadcastMessage('| Drag the answers and fill in the blanks |', '')
        else:
            ozoneEarth.visible = False
            ozonePlayer.visible = False
            ozoneInvaders.visible = False
            ozoneFact7.visible = False
            menu.visible = True
            ozoneLayerQuestions.visible = False
            ozoneLayerAnswers.visible = False
            ozonePart4.visible = False
            app.background = 'green'
            app.ozoneChallenge = False
            broadcastMessage ('| OZONE Badge Earned, Congrats! |', '')
            app.status = 'menu'
        
    
        
def broadcastMessage (value, value2):
    app.messageTimer = 90
    app.message = True
    message.visible = True
    messageLabel.value = value
    messageLabel2.value = value2
    
def geoThermChallenge():
    app.background = 'grey'
    app.status = 'geoChallenge'
    geoThermStart.visible = True
    broadcastMessage ('| Use WASD to connect the pipe to the bottom |', '')
    geoPipe.visible = True
    geoPipe.y2 = 200
    geoPipe2.centerY = 200
    geoPipe.x2 = 200
    geoPipe2.centerX = 200
    geoPipe2.visible = True
    app.geoChallenge = True

def solarPowerChallenge():
    app.background = 'limeGreen'
    app.status = 'solarChallenge'
    broadcastMessage ('| Use WASD to steer and accelerate your car |', '| Avoid obstacles and collect sunlight orbs |')
    app.solarChallenge = True
    solarOrb.visible = True
    solarCar.visible = True
    solarTrack1.visible = True
    solarLine1.visible = True
    solarCar.toFront()
    solarCourse1.toFront()
    solarFact1.toFront()
    solarFact1.visible = True
    solarBattery.visible = True
    solarCourse1.visible = True
    import random
    
def windPowerChallenge():
    app.background = 'skyBlue'
    app.status = 'windChallenge'
    windPowerMountains.visible = True
    bird.toFront()
    bird.visible = True
    app.windGravity = False
    app.windChallenge = True
    broadcastMessage ('| Use SPACEBAR to boost upward |', '| Do not hit the windmills |')
    
def ozoneLayerChallenge():
    app.background = rgb(6, 1, 63)
    menu.visible = False
    ozonePlayer.visible = True
    ozoneInvaders.visible = True
    ozoneEarth.visible = True
    app.status = 'ozoneChallenge'
    app.ozoneChallenge = True
    broadcastMessage("Shoot the CFC Orbs, don't get overun!", "Left/Right Arrow Keys to move, SPACE to shoot")

def ecosystemChallenge():
    app.background = "skyBlue"
    menu.visible = False
    app.status = 'ecosystemChallenge'
    app.ecosystemChallenge = True
    frog.visible = True
    ecoClouds.visible = True
    cursor.visible = True
    app.ecoFlyTimer = 200
    app.ecoFlyCount = 0
    app.ecoFliesPast = 0
    ecoHearts.visible = True
    for i in ecoHearts:
        i.visible = True
    ecoH1.visible = True
    ecoH2.visible = True
    ecoH3.visible = True
    ecoH4.visible = True
    ecoH5.visible = True
    broadcastMessage("Aim with mouse and click to attack", 'Do not let more than 5 flies get past you!')
    
def nextSolarFact ():
    if (solarFact1.visible == True):
        solarFact1.visible = False
        solarFact2.visible = True
        broadcastMessage("| Pay attention to the facts |", "| You will be quizzed at the end |")
        app.solarFact = 2
    elif (solarFact2.visible == True):
        solarFact2.visible = False
        solarFact3.visible = True
        app.solarFact = 3
    elif (solarFact3.visible == True):
        solarFact4.visible = True
        solarFact3.visible = False
        app.solarFact = 4
        solarCourse2.centerX  = 1148
    elif (solarFact4.visible == True):
        solarFact5.visible = True
        solarFact4.visible = False
        app.solarFact = 5
    elif (solarFact5.visible == True):
        solarFact6.visible = True
        solarFact5.visible = False
        app.solarFact = 6
    elif (solarFact6.visible == True):
        solarFact7.visible = True
        solarFact6.visible = False
        app.solarFact = 7
        solarCourse3.centerX  = 983
    elif (solarFact7.visible == True):
        solarFact8.visible = True
        solarFact7.visible = False
        app.solarFact = 8
    elif (solarFact8.visible == True):
        solarFact9.visible = True
        solarFact8.visible = False
        app.solarFact = 9    
    elif (solarFact9.visible == True):
        solarFact9.visible = False
        solarBattery.visible = False
        solarTrack1.visible = False
        solarLine1.visible = False
        solarCar.visible = False
        solarOrb.visible = False
        solarPowerQuestions.visible = True
        solarPowerAnswers.visible = True
        app.background = 'grey'
        broadcastMessage('| Drag the answers and fill in the blanks |', '')
        app.solarFact = 10
        if ((app.solarScore == 5) and (app.status == 'solarChallenge') and (app.solarFact == 10)):
            menu.visible = True
            solarPowerQuestions.visible = False
            solarPowerAnswers.visible = False
            solarPowerPart4.visible = False
            app.background = 'green'
            solarPowerBadgePart.fill = 'white'
            solarPowerBadgePart.border = 'gainsboro'
            solarPowerLabel.fill='white'
            solarPowerPart2.fill='orange'
            solarPowerPart3.fill='yellow'
            app.solarChallenge = False
            broadcastMessage ('| SOLAR Badge Earned, Congrats! |', '')
            app.status = 'menu'
            app.solarPower  = True
    
def solarOrbNext ():
    solarOrb.centerX = 450
    solarOrb.centerY  = random.randint (115, 285)
    while solarOrb.hitsShape(solarCourse1) == True and solarCourse1.visible == True:
        solarOrb.centerY = random.randint (115, 285)
    while solarOrb.hitsShape(solarCourse2) == True and solarCourse2.visible == True:
        solarOrb.centerY = random.randint (115, 285)
    while solarOrb.hitsShape(solarCourse3) == True and solarCourse3.visible == True:
        solarOrb.centerY = random.randint (115, 285)
    solarOrb.visible = True
    
def login(password):
    if ("i7" in password):
        app.geoTherm = True
        menu.visible = True
        geoThermPart4.visible = False
        geoPipe.visible = False
        geoPipe2.visible = False
        app.background = 'green'
        geoThermBadgePart.fill = 'white'
        geoThermBadgePart.border = 'gainsboro'
        geoThermLabel.fill='white'
        geoThermPart2.fill='orange'
        geoThermPart3.fill='yellow'
        app.geoChallenge = False
        geoThermStart.visible = False
        app.geoScore = 5
    if ("j8" in password):
        app.background = 'green'
        solarPowerBadgePart.fill = 'white'
        solarPowerBadgePart.border = 'gainsboro'
        solarPowerLabel.fill='white'
        solarPowerPart2.fill='orange'
        solarPowerPart3.fill='yellow'
        app.solarChallenge = False
        app.status = 'menu'
        app.solarPower  = True
        solarPowerPart4.visible = False
        app.solarScore = 5
    if ("d2" in password):
        windPowerBadgePart.fill = 'white'
        windPowerBadgePart.border = 'gainsboro'
        windPowerLabel.fill='white'
        windPowerPart4.visible = False
        app.windPower = True
    if ("jo2" in password):
        ozoneBadgePart.fill = 'white'
        ozoneBadgePart.border = 'gainsboro'
        ozoneLabel.fill='white'
        ozonePart2.fill='skyBlue'
        ozonePart3.fill='seaGreen'
        ozonePart4.visible = False
        ozoneBadge.remove(ozonePart4)
        app.ozoneLayer  = True
    if("ko" in password):
        app.ecosystem = True
        ###
        ecosystemPart4.visible = False
        ecosystemPart3.fill = rgb(71, 134, 71)
        
        ecosystemPart2 = Group (
            Oval (200, 300, 60, 50, fill=rgb(36, 182, 36)),
            Oval (175, 280, 20, 20, fill=rgb(36, 182, 36)),
            Oval (225, 280, 20, 20, fill=rgb(36, 182, 36)),
            Circle (175, 280, 6, fill='white'),
            Circle (225, 280, 6, fill='white'),
            Circle (175, 280, 4, fill='black'),
            Circle (225, 280, 4, fill='black'),
            )
        ecosystemLabel.fill = 'white'
        ecosystemBadge.remove(ecosystemPart4)
        ecosystemBadge.add(ecosystemPart2)
        ecosystemBadgePart.fill = 'white'
        ecosystemBadgePart.border = 'gainsboro'
        ecosystemPart3.toFront()
        ###
        

def generatePassword():
    app.password = ''
    app.keywords = []
    app.currentKeyword = ''
    app.password = app.password + str(random.randint(1, 100))
    app.password = app.password + app.letters[random.randint(0, 10)]
    if (app.geoTherm == True):
        app.keywords.append("i7")
    if (app.solarPower == True):
        app.keywords.append("j8")
    if (app.windPower == True):
        app.keywords.append("d2")
    if (app.ozoneLayer == True):
        app.keywords.append("jo2")
    if (app.ecosystem == True):
        app.keywords.append("ko")
    while (len(app.keywords) > 0):
        app.currentKeyword = app.keywords[len(app.keywords) - 1]
        app.keywords.remove(app.currentKeyword)
        app.password = app.password + app.currentKeyword
        app.password = app.password + app.letters[random.randint(0, 10)]
    app.password = app.password + str(random.randint(1, 100))
    app.password = app.password + app.letters[random.randint(0, 10)]
    print(app.password)
    passwordBox.visible = True
    passwordBox.toFront()
    passwordLabel.value = app.password
   
app.badgeAnimation = 1
app.badgeAnimation2 = 1
app.badgeAnimation3 = 1
app.badgeAnimation4 = 0.2
    
def menuBadgeAnimation():
    if (geoThermLabel.size == 15):
        geoThermPart3.height -= app.badgeAnimation * 1.5
        geoThermPart2.width += app.badgeAnimation*0.25
        geoThermPart3.centerY += app.badgeAnimation*0.75
        if (geoThermPart3.height<34.5):
            app.badgeAnimation = -1
        elif (geoThermPart3.height> 50):
            app.badgeAnimation = 1
    if (solarPowerLabel.size==15):
        solarPowerPart2.rotateAngle += 1
    if (windPowerLabel.size==15):
        windPowerPart3.rotateAngle += 2
    if (ozoneLabel.size == 15):
        if (ozonePart2.radius >= 33):
            app.badgeAnimation2 = -1
        if (ozonePart2.radius <= 30):
            app.badgeAnimation2 = 1
        ozonePart2.radius += 0.4*app.badgeAnimation2
    if (trophyLabel.size == 15):
        trophyBadgePart4.rotateAngle -= 3
        trophyBadgePart.borderWidth += app.badgeAnimation3
        if (trophyBadgePart.borderWidth >= 7):
            app.badgeAnimation3 = -0.2
        elif (trophyBadgePart.borderWidth <= 5):
            app.badgeAnimation3 = 0.2
    else:
        trophyBadgePart.borderWidth = 5
    if (ecosystemLabel.size == 15):
        if (ecosystemPart3.width >= 23):
            app.badgeAnimation4 = -0.2
        if (ecosystemPart3.width <= 20):
            app.badgeAnimation4 = 0.2
        ecosystemPart3.width += app.badgeAnimation4
        ecosystemPart3.height += app.badgeAnimation4

### Credits and Sources, BETA 0.5

# Coded on academy.cs.cmu.edu (Carnegie Mellon University Computer Science Academy) using CMU Graphics
# https://academy.cs.cmu.edu/about

# Luke Joseph, 2024

# INFO SOURCES:

# buisnessinsider.com
# energy.gov
# eia.gov
# epa.gov
# jpl.nasa.gov
# khanacademy.org
# nationalgeographic.org
# noaa.gov
# unep.org

# SOUNDTRACKS DOWNLOADED FROM PIXABAY

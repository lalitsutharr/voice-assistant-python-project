class Patient:

    Symptoms = {1: "Fever", 2: "Rashes", 3: "Itching", 4: "Weakness",
                5: "Cough", 6: "asthma", 7: "Shigella", 8: "influenza", 9: "meningitis"}
    cure = {1: {"Fever": "Take Paracetamol"}, 2: {"Rashes": "Take Cetrizine"}, 3: {"Itching": "Take Ceterizine"}, 4: {"weakness": "Take MultiVitamin"}, 5: {"cough": "Dextromethorphanl"}, 6: {
        "asthma": "albuterol (ProAir HFA, Ventolin HFA, others) "}, 7: {"Shigella": "ampicillin, trimethoprim / sulfamethoxazole (Bactrim, Septra ), ceftriaxone (Rocephin), orciprofloxacin"}, 8: {"influenza": "Rapivab (peramivir)"}, 9: {"meningitis": "cephalosporins"}}
# =======================================================================================================================
    question = {1: "fever more than two day ???\n", 2: "Are rashes spreading in whole body???\n", 3: "itching in whole body??\n", 4: "weakness whole day ????\n", 5: "Are you having Cough for more than 3 weeks?\n", 6: "Rapid worsening of shortness of breath or wheezing\nNo improvement even after using a quick-relief inhaler\nbreath, coughing or wheezing\n ",
                7: "dehydration,rectal bleeding, and invasion of the blood stream by the bacterium.?", 8: " Fever, cough, shaking chills, body aches, and extreme weakness are common symptoms?", 9: "Sudden feverSevere, headache that seems different than normalSeizures,Sensitivity to lightSleepinessLethargy,Skin rash?"}
    feedback = {1: "malaria.consult to doctor!!! !!!\n", 2: "you might be chikenpox.Spots: The spots develop in clusters and generally"
                "appear on the face, limbs, chest and stomach.They tend to be small, red, and itchy.Blisters: Blisters can develop on the top "
                "of the spots These can become very itchy.Clouding: Within about 48 hours, the blisters cloud over and start.A crust develops."
                "Healing: Within about 10 days, the crusts fall off on their own.!!!\n", 3: "tired Hydrocortisone cream in you"
                "itching part.\n", 4: "you got loose motion !!!\n", 5: "You may have got tuberculosis\nThere are two common tests"
                "for tuberculosis:\nSkin test. This is also known as the Mantoux tuberculin skin test. A technician injects a small"
                "amount of fluid into the skin of your lower arm. After 2 or 3 days, they’ll check for swelling in"
                "your arm.\n", 6: "consult your doctor as soon as possible", 7: "You may experience one or several symptoms of an"
                "infectious disease. It’s important to see a doctor if you have any chronic (ongoing) symptoms or symptoms that get"
                "worse over time.10mPeople with Shigella infection should drink plenty of fluids to prevent dehydration.People with"
                "bloody diarrhea should not use anti-diarrheal medication, such as loperamide (Imodium) or diphenoxylate with"
                "atropine (Lomotil). These medications may make symptoms worse.Antibiotics can shorten the time you have fever"
                "and diarrhea by about 2 days.Ciprofloxacin and azithromycin are two recommended oral antibiotics.", 8: "influenza"
                "Usually, youll need nothing more than rest and plenty of fluids to treat the flu. But if you have a severe"
                "infection or are at higher risk for complications, your doctor may prescribe an antiviral drug to treat the flu."
                " These drugs can include oseltamivir (Tamiflu), zanamivir (Relenza), peramivir (Rapivab) or baloxavir (Xofluza). These drugs may shorten your illness by a day or so and help prevent serious complications", 9: "Specialist to consult Specializes in treating diseases of the nervous system, which includes the brain, the spinal cord, and nerves"}
# =======================================================================================================================

    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender
        self.symptoms = []

    def setSymptoms(self):

        sym = []
        print()
        symptomCount = int(
            input("How many Symptoms Do you have? max = 9 : \t"))

        print("Choose symptoms:")

        for symptom in Patient.Symptoms:
            print(symptom, ": ", Patient.Symptoms[symptom])

        print()

        for x in range(0, symptomCount):
            ch = int(input())

            if ch < 1 or ch > 9:
                print("Invalid choice!!!")
                break

            sym.append(ch)

        self.symptoms = sym

    def display(self):

        print()
        print("Name of patient : ", self.name)
        print("Age of patient : ", self.age)
        print("Gender of patient : ", self.gender)

        print()

        for x in self.symptoms:
            print(Patient.cure[x])
        #===================asking question===================#
        ch_feedback = 0
        for x in self.symptoms:
            print(Patient.question[x])
            print("If yes press 1 else press 0")
            ch_feedback = int(input())
            if ch_feedback == 1:
                print(Patient.feedback[x])
            else:
                continue
        #====================================================#


name = input("Enter your name : \t")
age = int(input("Enter your age : \t"))
gender = input("Enter your gender(Male, Female or Other) : \t")

p = Patient(name, age, gender)
p.setSymptoms()
p.display()

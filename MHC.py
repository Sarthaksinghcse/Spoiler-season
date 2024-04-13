import tkinter as tk
from tkinter import scrolledtext, messagebox

class MentalHealthChatApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Mental Health Assistant")
        
        self.responses = {
            "hello": "Hello! I'm here to help as your Mental Health Chatbot.",
            "hii": "Hello! I'm here to help as your Mental Health Assistant.",
            "hi": "Hello! I'm here to help as your Mental Health Assistant.",
            "depression": "Alright, let's tackle this mood monster called depression! First off, take some deep breaths—pretend you're blowing out birthday candles, but there's no cake to share. Exercise is your new BFF; it's like a mood-boosting dance-off where you're the star. Fill up on good stuff—fruits, veggies, all the colorful foods that aren't Skittles. Sleep like you're prepping for a sleep Olympics—go for gold in snoozing! Dodge those mood-zapping triggers like they're bad karaoke nights. Chatting with a therapist can be like having a personal cheerleader for your brain. And hey, laughter's still the best medicine, so throw in some comedy breaks!",           
            "overthinking": "Alright, let's tackle overthinking like it's a never-ending playlist—time to hit the skip button! First, take some deep breaths—imagine you're blowing away those swirling thoughts like you're cleaning dust off old records. Exercise is like hitting the pause button on overthinking; it gives your mind a break and lets you focus on the here and now.Fill up on brain-boosting foods, maybe some omega-3-rich fish or colorful veggies to give your noggin a nutritional boost. Sleep like you're powering down for the night—turn off those overthinking circuits and hit the reset button. Try to dodge the overthinking triggers; it's like avoiding that one song that always gets stuck in your head.A therapist can be your playlist curator, helping you sort through those repetitive thoughts and find some new tunes to groove to. And hey, distract yourself with activities you love—whether it's jamming to music, diving into a hobby, or even just daydreaming. Remember, sometimes you've just got to change the track to shake off that overthinking groove!",
            "anxiety": "Alright, let's tackle this anxiety beast! First up, deep breaths—like you're trying to inflate a balloon with your lungs. Then, get those endorphins flowing with some exercise; think of it as a dance party with yourself (no judgment on the moves!). Eat your veggies and skip the caffeine rollercoaster—it's a wild ride you don't need. Sleep like you're hibernating, but without the fur and cave. Avoid those anxiety triggers like they're bad reality TV shows. Maybe try chatting with a therapist—they're like life coaches, but with better listening skills. And don't forget to sprinkle in some fun—laughter really is the best medicine!",
            "loneliness": "Alright, let's tackle this loneliness thing head-on! First, take some deep breaths—imagine you're inhaling good vibes and exhaling those lonely feels. Next up, get out there and do something you love, even if it's a solo dance party in your living room. Fill your plate with tasty, feel-good foods; maybe try cooking up a storm or ordering from your favorite spot. Sleep like you're in a cozy cocoon, because a good night's rest can do wonders for the soul.Reach out to friends, even if it's just a virtual coffee chat or a funny meme exchange. A therapist can be like a personal navigator for your emotional journey, helping you find your way back to connection. And remember, pets make great companions—they're like furry therapists with unconditional love. So, sprinkle in some self-love and fun activities to beat that loneliness blues!",
            "stress": "Alright, let's take on stress like it's a messy room—bit by bit, we'll tidy it up! First off, deep breaths—imagine you're deflating a stress balloon with each exhale. Exercise is your stress-busting superhero; think of it as your own personal Avengers team, but with more sweat. Eat foods that make you feel like you've got a mini vacation on a plate—think tropical fruits or your favorite comfort foods.Sleep is your secret weapon against stress, so aim for those Z's like they're the last piece of cake in the fridge. Try to dodge stress triggers like they're surprise pop quizzes. Chatting with a therapist can be like having a stress-busting sidekick, guiding you through tough times. And don't forget to sprinkle in some relaxation—whether it's a bubble bath or binge-watching your favorite show. You've got this!",
        }
        
        self.create_widgets()
        self.show_start_message()

    def create_widgets(self):
        self.conversation_area = scrolledtext.ScrolledText(self.root, width=150, height=30)
        self.conversation_area.grid(row=0, column=0, columnspan=2, padx=10, pady=10)

        self.input_label = tk.Label(self.root, text="User:")
        self.input_label.grid(row=1, column=0, padx=10, pady=5)

        self.user_input = tk.Entry(self.root, width=40)
        self.user_input.grid(row=1, column=1, padx=10, pady=5)
        self.user_input.bind("<Return>", self.get_response)

        self.send_button = tk.Button(self.root, text="Send", command=self.get_response)
        self.send_button.grid(row=1, column=2, padx=10, pady=5)

    def show_start_message(self):
        start_message = "Please start by typing 'Hi or Hello'"
        self.conversation_area.insert(tk.END, "Mental Health Assistant: " + start_message + "\n")

    def get_response(self, event=None):
        user_query = self.user_input.get().lower()  
        if user_query:
            self.conversation_area.insert(tk.END, "User: " + user_query + "\n")
            if user_query == "hi":
                self.conversation_area.insert(tk.END, "What are you feeling now: \nDepression \nAnxiety \nLoneliness \nStress" )
            elif user_query == "hii":
                self.conversation_area.insert(tk.END, "What are you feeling now: \nDepression \nAnxiety \nLoneliness \nStress" )    
            elif user_query == "hello":
                self.conversation_area.insert(tk.END, "What are you feeling now: \nDepression \nAnxiety \nLoneliness \nStress" )
            else:
                bot_response = self.get_bot_response(user_query)
                self.conversation_area.insert(tk.END, "Mental Health Assistant: " + bot_response + "\n")
                
            self.user_input.delete(0, tk.END)

    def get_bot_response(self, user_query):
        # Check for custom user-added questions and answers
        if user_query in self.responses:
            return self.responses[user_query]
        else:
            return "i'm not trained to provide advice on that specific topic. if you're struggling, please seek professional help."

if __name__ == "__main__":
    root = tk.Tk()
    app = MentalHealthChatApp(root)
    root.mainloop()

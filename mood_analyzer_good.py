import joblib
model = joblib.load('mood_analyzer\model3')
cv = joblib.load('mood_analyzer\count_vectorizer.pkl')



negative_text = ["""The alarm clock buzzed mercilessly, piercing through the comforting cocoon of sleep. Emily groaned and fumbled for the snooze button. Another day awaited her, and the weight of it felt almost unbearable.

Emily had been struggling with a persistent sense of sadness for quite some time. She couldn't pinpoint the exact cause; it was as if a cloud had settled over her, dimming the vibrancy of life. Her therapist had diagnosed her with depression, and she was doing her best to navigate it.

As she dragged herself out of bed, she wondered if today would be any different. With a heavy heart, she made her way to the bathroom. The mirror reflected a tired face, and the eyes that stared back at her seemed devoid of the sparkle they once held. Emily knew she needed to shake off this gloom, at least for a while.

After a quick shower and a rushed breakfast, Emily ventured out into the world. She had promised her friend, Sarah, that she'd meet her at the local park. Sarah, an eternal optimist, always seemed to radiate joy. Perhaps some of that radiance could rub off on her today.

The park was an oasis of tranquility, with the morning sun casting a warm glow over the trees and the chirping of birds filling the air. Emily spotted Sarah, who waved enthusiastically, her smile infectious. Emily couldn't help but smile back.

They chatted about life, and Sarah shared stories of her recent adventures. Emily found herself captivated by her friend's energy and enthusiasm. It was a stark contrast to the apathy she had been feeling lately.

As they strolled through the park, they encountered a group of children flying kites. Emily watched as the colorful kites danced in the sky, feeling a sense of wonder she hadn't experienced in a while. The simplicity and purity of the moment touched her, and she was grateful for the respite from her inner turmoil.

After saying goodbye to Sarah, Emily headed to a local café. She ordered her favorite coffee and settled into a corner with a book. Reading had always been a source of solace, and it transported her to different worlds, if only temporarily. The characters' triumphs and struggles resonated with her own.

Time passed quickly, and before she knew it, it was time to meet her therapist. Dr. Bennett's office was a safe space, where Emily could open up about her feelings without judgment. They discussed her recent experiences, and Dr. Bennett suggested some coping strategies. Emily left the session feeling a glimmer of hope, a small seed that maybe, just maybe, she could find her way out of the darkness.

In the evening, Emily decided to revisit an old hobby: painting. The canvas was blank, and the colors called out to her. As she painted, she poured her emotions onto the canvas, each brushstroke a reflection of her inner turmoil. By the time she finished, the artwork felt like a piece of her soul, a visual representation of her journey through sadness.

To unwind, Emily went for a long walk in the nearby woods. The trees whispered secrets of resilience, having weathered countless storms. She found comfort in their silent wisdom and appreciated the beauty of the natural world.

The day drew to a close, and Emily returned home. She lit some scented candles, played soft music, and took a moment to meditate. It was a practice she had recently adopted, a way to find stillness in the chaos of her mind.

As she lay in bed, she reflected on the day. It had been a rollercoaster of emotions, with moments of joy, sadness, and hope. She realized that life was a series of ups and downs, and her journey through depression was just one chapter.

Despite the sadness that still clung to her, Emily felt a glimmer of optimism. The day had reminded her that happiness was not a constant state but a series of fleeting moments. Perhaps, with time, those moments would become more frequent and enduring.

She closed her eyes, ready to face another day, knowing that each sunrise brought with it the promise of new beginnings. In her heart, she carried the hope that one day, she would rediscover the fullness of joy that life had to offer."""]
positive_text = ["""My day was absolutely fantastic! From the moment I woke up, I could feel the positive energy in the air. The sun was shining brightly, and I knew it was going to be a day filled with exciting adventures.

I started my morning with a delicious breakfast, and the aroma of fresh coffee added an extra touch of delight. With a full stomach and a smile on my face, I set out to conquer the day.

I decided to go for a long hike in the mountains, and the scenery was breathtaking. The crisp mountain air and the sound of birds singing in the trees made me feel truly alive. I reached the summit, and the panoramic view was a reward in itself.

After the hike, I met up with some close friends for a picnic by a serene lake. We laughed, shared stories, and enjoyed good food in the company of great people. It was a reminder of the importance of those special connections in life.

As the day transitioned into evening, I found myself at a beach bonfire with more friends. The crackling flames, the rhythmic sound of the waves, and the laughter of friends created the perfect ambiance for a memorable evening. We sang songs, roasted marshmallows, and shared our dreams.

Under a sky filled with a myriad of stars, I laid back on the sand and felt a profound sense of gratitude. It was a day where everything felt right, where I was in tune with the world around me, and where each moment was a treasure.

Now, as I reflect on my great day, I'm reminded that life is a precious gift. The simple joys and the beautiful moments are what make it all worthwhile. Today was a reminder that with a positive attitude and a heart full of appreciation, any day can be a great day."""]


def predict_text(text):
    x_predict = cv.transform(text).toarray()
    predictions = model.predict(x_predict)
    if predictions == 0:
        print('Tough days make you tougher. Brighter days are coming; hang in there!')

    elif predictions == 1:
        print('What a great day! Keep the positivity going and make every day as awesome as this one!')


def play_analyzer():
    while True:
        mood = input("Hello Welcome to the mood analyzer, here you can either choose to speak about your day,\n or use one of the predefined texts use 'me' for your day, 'positive' or 'negative' for the predefined ones\n please say 'see' to check out the predefined texts\n you can also use 'exit to leave. ")
        
        if mood.lower() == "positive" or mood.lower() == "1":
            predict_text(positive_text)

        elif mood.lower() == "negative" or mood.lower() == "2":
            predict_text(negative_text)

        elif mood.lower() == "me" or mood.lower() == "3":
            we_dont_know_yet = []
            self_day = input("How was your day? ")
            we_dont_know_yet.append(self_day)
            predict_text(we_dont_know_yet)

        elif mood.lower() == "see" or mood.lower() == "4":
            choice = input("Would you like to see the positive or the negative one? ")
            if choice.lower() == "positive" or mood.lower() == "1":
                print(positive_text)
            elif choice.lower()== "negative" or mood.lower() == "2":
                print(negative_text)

        elif mood.lower() == "exit" or mood.lower() == "5":
            print("Glad I could help")
            break



if __name__ == "__main__":
    play_analyzer()
    
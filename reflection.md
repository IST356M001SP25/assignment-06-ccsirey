# Reflection

Student Name:  name
Sudent Email:  email

## Instructions

Reflection is a key activity of learning. It helps you build a strong metacognition, or "understanding of your own learning." A good learner not only "knows what they know", but they "know what they don't know", too. Learning to reflect takes practice, but if your goal is to become a self-directed learner where you can teach yourself things, reflection is imperative.

- Now that you've completed the assignment, share your throughts. What did you learn? What confuses you? Where did you struggle? Where might you need more practice?
- A good reflection is: **specific as possible**,  **uses the terminology of the problem domain** (what was learned in class / through readings), and **is actionable** (you can pursue next steps, or be aided in the pursuit). That last part is what will make you a self-directed learner.
- Flex your recall muscles. You might have to review class notes / assigned readings to write your reflection and get the terminology correct.
- Your reflection is for **you**. Yes I make you write them and I read them, but you are merely practicing to become a better self-directed learner. If you read your reflection 1 week later, does what you wrote advance your learning?

Examples:

- **Poor Reflection:**  "I don't understand loops."   
**Better Reflection:** "I don't undersand how the while loop exits."   
**Best Reflection:** "I struggle writing the proper exit conditions on a while loop." It's actionable: You can practice this, google it, ask Chat GPT to explain it, etc. 
-  **Poor Reflection** "I learned loops."   
**Better Reflection** "I learned how to write while loops and their difference from for loops."   
**Best Reflection** "I learned when to use while vs for loops. While loops are for sentiel-controlled values (waiting for a condition to occur), vs for loops are for iterating over collections of fixed values."

`--- Reflection Below This Line ---`

I was able to handle the API calls section fairly easily, the one exception was the part, where the asserted value was different than where I came up with. I figured out that I just needed to go into the test section and change the expected value.

Moving onto the next part, I was able to complete the first step (review extraction) by calling the Google Places API and formatting the data as expected. However, I ran into issues with file paths that caused the unit tests to fail. Specifically, the test could not locate the expected cache/reviews.csv file, which I later realized was due to a mismatch between the path used in the code and the directory from which I was running the script.

Despite using the correct file structure and consulting both provided solutions and external help (including ChatGPT), I struggled to resolve the pathing issue consistently. I learned that relative paths in Python depend heavily on where the script is run from, and using os.path.join() with __file__ is a more reliable approach to making scripts portable. Despite learninjg about this option. I still wasn;t able to correctly connect the path. I still wasn't really able to figure out what my issue was in the end. That being said, I've never been the best at file paths so establishing a base area to path from will be helpful to me in the future.

Although I wasn’t able to complete all three steps by the deadline, this assignment helped me better understand how to work with APIs, JSON normalization, and the importance of managing file paths and directories properly in larger projects. It also showed me the value of breaking down the problem and seeking help when I got stuck.
import os
import openai
openai.api_key = os.getenv("OPENAI_API_KEY")  # change here if needed

system_en = open("DoT_system_prompt.txt", encoding="utf-8").read()
user_template_en = "Patient Message: {}"
system_zh = open("DoT_system_prompt_zh.txt", encoding="utf-8").read()
user_template_zh = "患者陈述：{}"

# English version
test_user_message = "Lately I have been extremely unhappy for no apparent reason. I feel empty almost all the time. It is like nothing can give me genuine joy anymore. I also feel alone a lot, even though I do have friends and close friends. Whenever I try to imagine my future all I see is one full of obstacles. I have become so consumed in sadness and I do not know how to deal anymore. I feel so confused and I do not understand myself anymore."
completion = openai.ChatCompletion.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "system", "content": system_en},
    {"role": "user", "content": user_template_en.format(test_user_message)}
  ]
)

print(completion.choices[0].message)

# Chinese version
test_user_message = "最近我莫名其妙地非常不开心。我几乎总是感到空虚。好像再也没有什么能给我真正的快乐了。我也经常感到孤独，即使我有朋友和亲密的朋友。每当我试着想象我的未来时，我看到的都是充满障碍的未来。我已经被悲伤吞噬了，我不知道该如何处理。我感到很困惑，我不再了解自己了。"
completion = openai.ChatCompletion.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "system", "content": system_zh},
    {"role": "user", "content": user_template_zh.format(test_user_message)}
  ]
)

print(completion.choices[0].message)
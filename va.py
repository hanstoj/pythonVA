import wolframalpha

input = raw_input("Question: ")
app_id = ________
client = worlframealpha.Client(app_id)

res = client.query(input)
answer = next(res.results).text

print answer

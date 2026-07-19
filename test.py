import google.generativeai as genai

genai.configure(api_key="AQ.Ab8RN6KpuF3xpm2QL356qGpsgx8NQx72dmLz5-Bw1ARWuTsucA")

print("Available models:\n")

for m in genai.list_models():
    print(m.name)
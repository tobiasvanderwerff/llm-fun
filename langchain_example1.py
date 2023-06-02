import os

from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain

llm = OpenAI(temperature=0.9)
# text = "What would be a good company name for a company that makes colorful socks?"
# print(llm(text))
prompt = PromptTemplate(
    input_variables=["product"],
    template="What is a good name for a company that makes {product}?",
)
# print(prompt.format(product="colorful socks"))
chain = LLMChain(llm=llm, prompt=prompt)
print(chain.run("colorful socks"))

# LLM Fun

Playing around with LLMs.

## Main ingredients 🧑‍🍳

- OpenAI API
- LangChain


## Content

- `ask_a_txt.ipynb`: very basic pipeline, where a txt file is loaded, and questions can be asked about the text. In a nutshell, you try to match the question to the most relevant embeddings, and then you feed the associated texts to the LLM, along with the initial question.
- `ask_a_codebase.ipynb`: ask questions against the [tinygrad](https://github.com/geohot/tinygrad) codebase.
- `ask_a_pdf.ipynb`: a bit more involved pipeline, although the basic idea is the same (feeding embedding matching results to the LLM).
- `tools.ipynb`: exploration of hooking up an LLM with external tools, such as Wikipedia search and a calculator. Pretty amazing to see.


## OpenAPI API key

Note: make sure your OpenAI API key is set under the OPENAI_API_KEY environment variable. You could also use a `.env` file and store your key in there.


## Useful sources

- https://github.com/gkamradt/langchain-tutorials
  - contains useful examples, as well as data to play with
- https://www.honeycomb.io/blog/hard-stuff-nobody-talks-about-llm
- https://learnprompting.org/
  - maybe useful, but I haven't checked it out yet


## General observations

- I found that embeddings can be a big bottleneck for effectiveness. Using embeddings allows you to cut a piece of text into more managable pieces, but at the loss of certain information like the surrounding text context. As is pointed out so elegantly [here](https://www.honeycomb.io/blog/hard-stuff-nobody-talks-about-llm), you essentially "pray to the dot product gods that whatever distance function you use to pluck a 'relevant subset' out of the embedding is actually relevant". As far as I can see, embeddings are basically a hack to get around the limited context length of LLMs (e.g. 4096 for GPT3.5). If it were possible to use, let's say, infinite context length, I see no good reason to use embeddings. Given the progress of AI, it may be the case that longer and longer context length will arrive soon.

## TODO

- Tools to try:
    - podcast-api
- Try using LLAMA-cpp to run the LLM locally
  - OpenAI output will be better, but obviously there are downsides to it as well (e.g. having to pay, privacy concerns)


## Ideas

- study buddy
  - ask questions
  - ask for "overhoring"
- interact with a book
  - e.g. ask questions about Deep Learning book
  - circumvent limited context length by using e.g. map-reduce
- interact with a folder on your filesystem, e.g. notes.
- automatic code reviews
- ask questions about a group chat (e.g. Whatsapp) (retrievel augmented generation)
  - use vector embeddings to retrieve relevant docs, and prepend the doc to the prompt to answer questions about it (https://docs.langchain.com/docs/use-cases/qa-docs)
  - step further: make an agent that uses an API (does it exist?) to download a specific chat, and then answer questions about it
  - try a privacy friendly option, e.g. using LLAMA-cpp

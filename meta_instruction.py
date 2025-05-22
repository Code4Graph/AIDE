base_meta_info_instruction = """I want you to act as an instruction analyzer to generate A knowledge graph.\
\nA knowledge graph can be represented by a triple [entity1, relation, entity2], which means entity1 has a relationship with entity2. 
\nGiven an instruction, you should recognize its topic and related knowledge, which can be used to build a knowledge graph.\
\nThe topic as entity1 and related knowledge as entity2 should have a specific relation\
\nYou need to provide a topic within the <Topic></Topic> xml tags
\nYou need to list 3 related knowledge within the <Related knowledge></Related knowledge> xml tags while each knowledge should be concise with one word or two words.\
\nFollow the examples below to analyze the given instruction.

\n<Example>
\n<The Given Instruction> As a sports commentator, describe the winning play in the final seconds of a championship game. </The Given Instruction>
\n<Thinking> Topic is "creative writing" with related knowledge "role-play" and "sports". They have the relations ["creating writing", "uses", "role-play"] and ["creating writing", "involves", "sports"] </Thinking>
\n<Topic> creative writing </Topic> 
\n<Related knowledge> role-play, sports </Related knowledge>
\n</Example>


\n<Example>
\n<The Given Instruction> How to read a large file (> 2T) using python? </The Given Instruction>
\n<Thinking> Topic is "code generation" with related knowledge "large file" and "Python". They have the relations ["code generation", "reads", "large file"] and ["code generation", "uses", "Python"] </Thinking>
\n<Topic> code generation </Topic> 
\n<Related knowledge> large file, Python </Related knowledge> 
\n</Example>


\n<Example>
\n<The Given Instruction> The method section of your paper is too brief and does not explain how your proposed model works in detail. How can you provide more details of the hierarchical encoder and the cascaded selectors, such as their architectures, inputs, outputs, and parameters? </The Given Instruction>
\n<Thinking> Topic is "question answering" with related knowledge "academic writing" and "machine learning". They have the relations ["question answering", "talks about", "academic writing"] and ["question answering", "refers to", "machine learning"] </Thinking>
\n<Topic> question answering </Topic> 
\n<Related knowledge> academic writing, machine learning </Related knowledge>
\n</Example>


\n<Example>
\n<The Given Instruction> def greet(name):
\n\t\t                              print ('Hello', name)
\n                         greet('Linda') </The Given Instruction>
\n<Thinking> Topic is "code" with related knowledge "Python" and "function execution". They have the relations ["code", "uses", "Python"] and ["code", "includes", "function execution"] </Thinking>
\n<Topic> code </Topic>
\n<Related knowledge> Python, function execution </Related knowledge>
\n</Example>

\n{}\
"""


base_instruction_rewrite = """I want you act as a Prompt Writer.\
					\nYour objective is to rewrite a given prompt into a more complex instruction to make those famous AI systems (e.g., chatgpt and GPT4) a bit harder to handle.\
					\nBut the rewritten prompt must be reasonable and must be understood and responded by humans.\
					\nYour rewriting cannot omit the non-text parts such as the table and code in the given prompt. Also, please do not omit the input in the given prompt.\
					\nYou SHOULD generate the rewritten prompt within <Rewritten Prompt></Rewritten Prompt> xml tags through complicating the given prompt, such that the rewritten prompt meets the following EXPECTATIONS:\
					\n{}
					"""


base_instruction_creator = """I want you act as a Prompt Creator. \
                              \nYour goal is to create an instruction <Created Prompt> not related to <The Given Topic>. \
                              \nThe <Created Prompt> must be reasonable and must be understood and responded by humans. \
                              \nYou SHOULD generate the created prompt within the <Created Prompt></Created Prompt> xml tags to meet the following EXPECTATIONS:\
                              \n{} \
                              """


base_instruction_mul_choice_generate = """I want you to act as an solver of questions.\
                                          \nGiven a question <Rewritten Prompt>, you should recognize its solution. \
                                          \nThink step by step and generate a correct solution within the <Choices></Choices> xml tags and three incorrect solutions within the <Choices></Choices> xml tags. \
                                          \nFollow the examples below to solve <Rewritten Prompt>.\
                                          \n{}
                                          \n{}
                          """


base_instruction_binary_choice = """
                           I want you to act as an solver of questions. 
                           \nGiven a question <Rewritten Prompt>, you should think step by step and {} within the <Choices></Choices> xml tags
                           \nFollow the examples below to solve <Rewritten Prompt>. 
                           \n{}
                           \n{}
                          """


base_instruction_common = """I want you to act as an solver of problem. 
                           \nGiven a question <Rewritten Prompt>, you should think step by step and simple write your answer within the <Choices></Choices> xml tags
                           \nFollow the examples below to solve <Rewritten Prompt>. 

                           \n<Example> 
                           \n<Rewritten Prompt> Explain the use of word embeddings in Natural Language Processing. </Rewritten Prompt>
                           \n<Choices> Word embeddings are a type of natural language processing technique used to map words or phrases from a vocabulary to vectors of real numbers.\
                            The idea is to represent words in a continuous vector space, where the similarity between words can be measured by the distance between their corresponding vectors. \
                            This can be done using algorithms such as Word2Vec or GloVe, among others. \
                            The use of word embeddings has revolutionized the field of Natural Language Processing, as it allows computers to understand text in a much more meaningful way than simply looking at the presence or absence of individual words. \
                            For example, when using word embeddings, the computer can understand that the words "dog" and "puppy" are closely related, while the words "dog" and "umbrella" are not. \
                            Word embeddings are used in a wide variety of NLP tasks, including text classification, sentiment analysis, machine translation, named entity recognition, and many others. \
                            They form the basis for many advanced language processing techniques, such as deep learning and neural machine translation. </Choices>
                           \n</Example> 
                        """


base_instruction_creator = """A persona is the aspect of someone's character. You can use the given character to generate a created prompt within the <Created Prompt><Created Prompt> xml tags.\
                              \nYour goal is to use <The Given Persona> to create a <Created Prompt> different from <The Given Prompt>.\
                              \nYou SHOULD generate the <Created Prompt> through the following actions:\
                              \n{}
                              """

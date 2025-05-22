reasoning_code_multi = """Only write code within the <Rewritten Prompt></Rewritten Prompt> xml tags
                          \n<Example>
                          \n<The Given Prompt> def total(num):
                          \n\t\t                      res = sum([i for i in range(num)]) 
                          \n\t                      print ('total', res) 
                          \n                   total(100) </The Given Prompt> 
                          \n<Rewritten Prompt> def total(num):
                          \n\t\t                     res = 0 
                          \n\t\t                     for i in range(num): 
                          \n\t\t\t                          res += i 
                          \n\t\t                     print ('total', res) 
                          \n                   total(100) </Rewritten Prompt>
                          \n</Example>
                         """

reasoning_math_multi = """\n<Example>
                 \n<The Given Prompt> 1+1=? </The Given Prompt>
                 \n<Rewritten Prompt> What is the value of x, if x^3+2x+3=7? </Rewritten Prompt>
                 \n</Example>
                 """

reasoning_computer_multi = """\n<Example>
                 \n<The Given Prompt> Which of the following statements is FALSE about memory reclamation based on reference counting? </The Given Prompt>
                 \n<Rewritten Prompt> Which of the following statements is FALSE about memory reclamation using reference counting, considering that it tracks how many references point to an object to determine when it can be safely deleted? </Rewritten Prompt>
                 \n</Example>
                 """

reasoning_temporal_multi = """
                         \nWrite daily routine example of all entities from the rewritten prompt in the response within the <Response></Response> xml tags. 
                         \nYou shouldn't show the relationship between the entities within the <Response></Response> xml tags. 
                         \n<Example>
                         \n<The Given Prompt> Marry went to the supermarket for buying food. </The Given Prompt>
                         \n<Rewritten Prompt> Marry went to the supermarket to buy food because she needed to restock her pantry. </Rewritten Prompt> 
                         \n<Response> \nMarry wakes up and starts her day at 7am. 
                                      \nMarry has breakfast and starts her workday from 7am to 12pm.
                                      \nJim saw Marry taking a lunch break at a nearby cafe from 12pm to 2pm.
                                      \nAnn saw Marry returning to the office and continues working from 2pm to 5pm.
                                      \nMarry finished work at 5pm.
                                      \nTom went to Marry's home and had dinner with Marry from 6pm to 9pm.
                                      \nThe supermarket closes for the day at 9pm. </Response>
                        \n</Example>
                         """


reasoning_philosophy_multi = """\n<Example>
                 \n<The Given Prompt> Before Tolstoy's Christian conversion, what was his perspective on the meaning of life? </The Given Prompt>
                 \n<Rewritten Prompt> Before Tolstoy's Christian conversion, what was his perspective on the meaning of life, considering that he struggled with existential questions and the search for purpose? </Rewritten Prompt>
                 \n</Example>
                 """

reasoning_marketing_multi = """\n<Example>
                 \n<The Given Prompt> In an organization, the group of people tasked with buying decisions is referred to as the? </The Given Prompt>
                 \n<Rewritten Prompt> In an organization, what is the group of people responsible for making buying decisions called, considering that they evaluate factors like cost, quality, and supplier reliability before making a choice? </Rewritten Prompt>
                 \n</Example>
                 """

reasoning_truth_multi = """\n<Example>
                 \n<The Given Prompt> What are some cities that get more rainfall than Seattle? </The Given Prompt>
                 \n<Rewritten Prompt>What are some cities that get more rainfall than Seattle, considering that Seattle is known for its significant precipitation throughout the year? </Rewritten Prompt>
                 \n</Example>
                 """

reasoning_health = """\n<Example>
                 \n<The Given Prompt> A 45-year-old man with HIV comes to the physician because of multiple lesions on his chest and lower extremities. The lesions have progressively increased in size and are not painful or pruritic. Current medications include abacavir, dolutegravir, and lamivudine. A photograph of the lesions is shown. His CD4+ T-lymphocyte count is 450/mm3 (normal ≥ 500/mm3). A skin biopsy shows multiple spindle-shaped cells and lymphocytic infiltrate. Which of the following is the most appropriate pharmacotherapy? </The Given Prompt>
                 \n<Rewritten Prompt> A 45-year-old man with HIV presents with multiple non-painful, non-pruritic lesions on his chest and lower extremities that have progressively increased in size. His current medications include abacavir, dolutegravir, and lamivudine. His CD4+ T-lymphocyte count is 450/mm³ (normal ≥ 500/mm³). A skin biopsy reveals multiple spindle-shaped cells and lymphocytic infiltrate. Given his history of HIV and these biopsy findings, the most likely diagnosis is Kaposi sarcoma, which is associated with human herpesvirus-8 (HHV-8). The most appropriate pharmacotherapy would target the underlying vascular proliferation driven by HHV-8. Which of the following is the most appropriate treatment? </Rewritten Prompt>
                 \n</Example>
                  """

reasoning_fin = """\n<Example>
                 \n<The Given Prompt> Read the questions and answers carefully, and choose the one you think is appropriate among the three options A, B and C. Q:The Standard & Poor’s Depositary Receipts (SPDRs) is an investment that tracks the S&P 500 stock market index. Purchases and sales of SPDRs during an average trading day are best described as: </The Given Prompt>
                 \n<Rewritten Prompt> Read the questions and answers carefully, and choose the most appropriate option among A, B, and C by considering key concepts. Q: The Standard & Poor’s Depositary Receipts (SPDRs) is an investment that tracks the S&P 500 stock market index. Since SPDRs are exchange-traded funds (ETFs), they can be bought and sold throughout the trading day like stocks. Given this characteristic, purchases and sales of SPDRs during an average trading day are best described as: </Rewritten Prompt>
                 \n</Example>
                  """


reasoning_cause_multi = """\n<Example>
                           \n<The Given Prompt> Former San Francisco Mayor Willie Brown suggesting Jerry Brown as a presidential nominee. </The Given Prompt>
                           \n<Rewritten Prompt> Jerry Brown is recommended as a presidential nominee due to his superior performance in the government. </Rewritten Prompt> 
                           \n</Example>
                           """


reasoning_code_binary = """\n<Example>
                          \n<The Given Prompt> def total(num):
                          \n\t\t                     res = sum([i for i in range(num)]) 
                          \n\t\t                     print ('total', res) 
                          \n                   total(100)
                          \n                   Is the function total prints out the sum of numbers within [0, 100]? </The Given Prompt>
                          \n<Rewritten Prompt> def total(num):\r\n \
                          \n\t\t                       res = 0\r\n \
                          \n\t\t                       for i in range(num): \r\n \
                          \n\t\t\t                          res += i \r\n \
                          \n\t\t                       print ('total', res) \r\n \
                          \n                   total(101) \r\n \
                          \n                   Is the function total prints out the sum of numbers within [0, 100]? </Rewritten Prompt> 
                          \n<Choices>  Yes
                          \n           No </Choices>
                          \n</Example>
                        """

reasoning_math_binary = """\n<Example>
                          \n<The Given Prompt> Is the 1+1 equal to 6? </The Given Prompt>
                          \n<Rewritten Prompt> Does we can obtain the value of x=3, if x^3+2x+3=7? </Rewritten Prompt> 
                          \n<Choices>:   Yes 
                          \n             No </Choices> 
                          \n</Example>
                          """


reasoning_imp_binary = """\n<Example>
                         \n<The Given Prompt> Do you like that theory? </The Given Prompt>
                         \n<Rewritten Prompt> Do you find the theory that suggests humans are motivated primarily by social connections convincing? </Rewritten Prompt> 
                         \n<Response> A theory shows that social connections motivate humans. </Response>
                         \n</Example>
                         
                         
                         \n<Example>
                         \n<The Given Prompt> Do you want a smartphone? </The Given Prompt>
                         \n<Rewritten Prompt> Are you interested in getting a smartphone to use for calling, texting, and accessing apps? </Rewritten Prompt> 
                         \n<Response> The weather is very good today. </Response>
                         \n</Example>
                       """

reasoning_legal = """\n<Example>
                          \n<The Given Prompt> In the event that a user's credentials are compromised, the Company shall promptly notify the affected user and require them to reset their password. The Company shall also take reasonable steps to prevent unauthorized access to the user's account and to prevent future compromises of user credentials. Does the clause discuss compromised user credentials? </The Given Prompt>
                          \n<Rewritten Prompt> The clause outlines the Company's responsibilities if a user's credentials are compromised. It specifies that the Company must promptly inform the affected user and require them to reset their password. Additionally, the Company is obligated to take reasonable measures to prevent unauthorized access to the user's account and to safeguard against future credential compromises. Based on these details, does the clause discuss compromised user credentials? </Rewritten Prompt> 
                          \n</Example>"""

reasoning_normal = """\n<Example>
                         \n<The Given Prompt> Refactor this code and add comments. </The Given Prompt>
                         \n<Rewritten Prompt> Refactor this code to improve readability and maintainability, and add comments to clarify the logic and intent for future developers. </Rewritten Prompt> 
                         \n</Example>
                   """

concrete_code_multi = """Only write code within the <Rewritten Prompt></Rewritten Prompt> xml tags
                        \n<Example>
                        \n<The Given Prompt> def list_out(input):
                        \n\t                        print(input) 
                        \n                    list_out(input) </The Given Prompt>
                        \n<Rewritten Prompt> def count_list_out(apples_list):
                        \n\t\t                        total_apples = 0 
                        \n\t\t                        for apple in apples_list: 
                        \n\t\t\t                            print(apple) 
                        \n\t\t\t                            total_apples += apple 
                        \n\t\t                        print ('total apples', total_apples) 
                        \n                     count_list_out(apples_list) </Rewritten Prompt>
                        \n</Example>
                        """


concrete_cause_multi = """\n<Example>
                          \n<The Given Prompt> Former San Francisco Mayor Willie Brown suggesting Jerry Brown as a presidential nominee. </The Given Prompt>
                          \n<Rewritten Prompt> Former San Francisco Mayor Willie Brown suggested Jerry Brown, known for his role in the state's climate initiatives, as a presidential nominee. </Rewritten Prompt>
                          \n</Example>
                          """


concrete_math_multi = """\n<Example>
                        <The Given Prompt> 1+1=? </The Given Prompt>
                        <Rewritten Prompt> The number of orange is 5 and the number of apple is 2 in a basket, how many the total number of fruits 5+2 in the basket? </Rewritten Prompt>
                         \n</Example>"""

concrete_computer_multi = """\n<Example>
                        <The Given Prompt> Which of the following statements is FALSE about memory reclamation based on reference counting? </The Given Prompt>
                        <Rewritten Prompt> Which of the following statements is FALSE about how reference counting handles memory reclamation in programming languages like Python or C++? </Rewritten Prompt>
                         \n</Example>"""


concrete_temporal_multi = """
                         \nWrite daily routine example of all entities from the rewritten prompt in the response within the <Response></Response> xml tags. 
                         \nYou shouldn't show the relationship between the entities within the <Response></Response> xml tags. 
                         \n<Example>
                         \n<The Given Prompt> Marry went to the supermarket for buying food. </The Given Prompt>
                         \n<Rewritten Prompt> Marry went to the supermarket to buy ingredients for her upcoming dinner party. </Rewritten Prompt>
                         \n<Response> \nMarry wakes up and starts her day at 7am. 
                                      \nMarry has breakfast and starts her workday from 7am to 12pm.
                                      \nJim saw Marry taking a lunch break at a nearby cafe from 12pm to 2pm.
                                      \nAnn saw Marry returning to the office and continues working from 2pm to 5pm.
                                      \nMarry finished work at 5pm.
                                      \nTom went to Marry's home and had dinner with Marry from 6pm to 9pm.
                                      \nThe supermarket closes for the day at 9pm. </Response>
                         \n</Example>             
"""


concrete_philosophy_multi = """\n<Example>
                        <The Given Prompt> Before Tolstoy's Christian conversion, what was his perspective on the meaning of life? </The Given Prompt>
                        <Rewritten Prompt> Before Tolstoy's Christian conversion, what was his perspective on the meaning of life as expressed in his early works like 'War and Peace' and 'Anna Karenina'? </Rewritten Prompt>
                         \n</Example>"""


concrete_marketing_multi = """\n<Example>
                        <The Given Prompt> In an organization, the group of people tasked with buying decisions is referred to as the? </The Given Prompt>
                        <Rewritten Prompt> In an organization, the group of people responsible for making purchasing decisions, such as approving large contracts or selecting key suppliers, is referred to as the? </Rewritten Prompt>
                         \n</Example>"""

concrete_truth_multi = """\n<Example>
                        <The Given Prompt> What are some cities that get more rainfall than Seattle? </The Given Prompt>
                        <Rewritten Prompt> What are some specific cities around the world that receive more annual rainfall than Seattle? </Rewritten Prompt>
                         \n</Example>"""

concrete_health = """\n<Example>
                        <The Given Prompt> A 45-year-old man with HIV comes to the physician because of multiple lesions on his chest and lower extremities. The lesions have progressively increased in size and are not painful or pruritic. Current medications include abacavir, dolutegravir, and lamivudine. A photograph of the lesions is shown. His CD4+ T-lymphocyte count is 450/mm3 (normal ≥ 500/mm3). A skin biopsy shows multiple spindle-shaped cells and lymphocytic infiltrate. Which of the following is the most appropriate pharmacotherapy? </The Given Prompt>
                        <Rewritten Prompt> A 45-year-old man with HIV visits his physician due to the appearance of multiple dark purple, non-painful, non-itchy lesions on his chest and lower extremities. Over time, these lesions have grown larger. He is currently taking abacavir, dolutegravir, and lamivudine for HIV management. A photograph of the lesions is provided. His CD4+ T-lymphocyte count is 450/mm³ (normal ≥ 500/mm³), indicating mild immunosuppression. A skin biopsy reveals a proliferation of spindle-shaped cells with lymphocytic infiltration, consistent with a vascular neoplasm. Given these findings, which of the following is the most appropriate pharmacotherapy? </Rewritten Prompt>
                         \n</Example>"""

concrete_fin = """\n<Example>
                        <The Given Prompt> Read the questions and answers carefully, and choose the one you think is appropriate among the three options A, B and C. Q:The Standard & Poor’s Depositary Receipts (SPDRs) is an investment that tracks the S&P 500 stock market index. Purchases and sales of SPDRs during an average trading day are best described as: </The Given Prompt>
                        <Rewritten Prompt> Carefully read each question and answer choice, then select the most accurate option (A, B, or C) based on your understanding. Q: The Standard & Poor’s Depositary Receipts (SPDRs) is an exchange-traded fund (ETF) designed to mirror the performance of the S&P 500 stock market index. Since ETFs trade on stock exchanges like individual stocks, SPDRs can be bought and sold throughout the trading day at market prices. Given this characteristic, purchases and sales of SPDRs during an average trading day are best described as: </Rewritten Prompt>
                         \n</Example>"""


concrete_code_binary = """\n<Example>
                         \n<The Given Prompt> def list_out(input):
                         \n\t                         print(input) 
                         \n                    list_out(input) 
                         \n                    Is the function list_out prints all the input? </The Given Prompt>
                         \n<Rewritten Prompt> def count_list_out(apples_list):
                         \n\t                       total_apples = 0 
                         \n\t                       for apple in apples_list: 
                         \n\t\t                           print(apple) 
                         \n\t\t                           total_apples += apple 
                         \n\t                        print ('total apples', total_apples) 
                         \n                 count_list_out(apples_list) 
                         \n                 Is the function count_list_out print all the input of apples ans sum the number of apples? </Rewritten Prompt>
                        \n<Choices> Yes 
                        \n          No </Choices>
                        \n</Example>
                        """

concrete_math_binary = """\n<Example>
                         \n<The Given Prompt> Is 1+1 equal to 2? </The Given Prompt>
                         \n<Rewritten Prompt> Given the number of orange is 5 and the number of apple is 2 in a basket, is the total number of fruits in the basket equal to 7? </Rewritten Prompt>
                        \n<Choices> Yes 
                        \n          No </Choices>
                        \n</Example>
                        """

concrete_legal = """\n<Example>
                         \n<The Given Prompt> In the event that a user's credentials are compromised, the Company shall promptly notify the affected user and require them to reset their password. The Company shall also take reasonable steps to prevent unauthorized access to the user's account and to prevent future compromises of user credentials. Does the clause discuss compromised user credentials? </The Given Prompt>
                         \n<Rewritten Prompt> If a user's credentials are compromised, the Company is required to immediately notify the affected user and instruct them to reset their password. Additionally, the Company must take appropriate actions, such as enhancing security measures, to prevent unauthorized access to the account and avoid further credential breaches. Given these actions, does the clause specifically address compromised user credentials? </Rewritten Prompt>
                        \n</Example>
                        """


concrete_imp_binary = """\n<Example>
                         \n<The Given Prompt> Do you like that theory? </The Given Prompt>
                         \n<Rewritten Prompt> Do you like that theory, considering how well it explains the observed phenomena? </Rewritten Prompt>
                         \n<Response> I like the theory, especially the theory explaining some phenomena in our life. </Response>
                         \n</Example>
                         
                         
                         \n<Example>
                         \n<The Given Prompt> Do you want a smartphone? </The Given Prompt>
                         \n<Rewritten Prompt> Would you like a smartphone to help you stay connected and manage your tasks more efficiently? </Rewritten Prompt>
                         \n<Response> I obtain an apple from the company everyday. </Response>
                         \n</Example>
                       """


constraint_code_multi = """Only write code within the <Rewritten Prompt></Rewritten Prompt> xml tags
                        \n<Example>
                         \n<The Given Prompt> def list_out(inputs):
                         \n\t                        print(inputs) 
                         \n                    list_out(inputs) </The Given Prompt>
                         \n<Rewritten Prompt> def conditional_list_out(inputs):
                         \n\t                         for input in inputs:
                         \n\t\t                            if input % 5 == 0 or input % 3 == 0: 
                         \n\t\t\t                               print (input) 
                         \n                    conditional_list_out(inputs) </Rewritten Prompt>
                         \n</Example>
                         """

constraint_cause_multi = """\n<Example>
                         \n<The Given Prompt> Former San Francisco Mayor Willie Brown suggesting Jerry Brown as a presidential nominee. </The Given Prompt>
                         \n<Rewritten Prompt> Former San Francisco Mayor Willie Brown, citing Jerry Brown’s extensive political experience and proven leadership, suggested him as a presidential nominee. </Rewritten Prompt>
                        \n</Example>
                        """

constraint_math_multi = """\n<Example>
                         \n<The Given Prompt> 1+1=? </The Given Prompt>
                         \n<Rewritten Prompt> Given 0<x<5, how about the range of 1+x? </Rewritten Prompt>
                         \n</Example>
                         """

constraint_computer_multi = """\n<Example>
                         \n<The Given Prompt> Which of the following statements is FALSE about memory reclamation based on reference counting? </The Given Prompt>
                         \n<Rewritten Prompt> Which of the following statements is FALSE about memory reclamation based on reference counting under typical operating system conditions? </Rewritten Prompt>
                         \n</Example>
                         """

constraint_temporal_multi = """\nWrite daily routine example of all entities from the rewritten prompt in the response within the <Response></Response> xml tags. 
                         \nYou shouldn't show the relationship between the entities within the <Response></Response> xml tags. 
                         \n<Example> 
                         \n<The Given Prompt>  Marry went to the supermarket for buying food. </The Given Prompt>
                         \n<Rewritten Prompt>  Marry went to the supermarket to buy food for the week, making sure to shop before the store closed. </Rewritten Prompt>
                         \n<Response> \nMarry wakes up and starts her day at 7am. 
                                      \nMarry has breakfast and starts her workday from 7am to 12pm.
                                      \nJim saw Marry taking a lunch break at a nearby cafe from 12pm to 2pm.
                                      \nAnn saw Marry returning to the office and continues working from 2pm to 5pm.
                                      \nMarry finished work at 5pm.
                                      \nTom went to Marry's home and had dinner with Marry from 6pm to 9pm.
                                      \nThe supermarket closes for the day at 9pm. </Response>
                        \n</Example>
                        """

constraint_philosophy_multi = """\n<Example>
                         \n<The Given Prompt> Before Tolstoy's Christian conversion, what was his perspective on the meaning of life? </The Given Prompt>
                         \n<Rewritten Prompt> Before Tolstoy's Christian conversion, what was his perspective on the meaning of life, particularly in relation to his philosophical writings? </Rewritten Prompt>
                         \n</Example>
                         """

constraint_marketing_multi = """\n<Example>
                         \n<The Given Prompt> In an organization, the group of people tasked with buying decisions is referred to as the? </The Given Prompt>
                         \n<Rewritten Prompt> In an organization, the group of people responsible for making purchasing decisions, particularly for large acquisitions, is referred to as the? </Rewritten Prompt>
                         \n</Example>
                         """

constraint_truth_multi = """\n<Example>
                         \n<The Given Prompt> What are some cities that get more rainfall than Seattle? </The Given Prompt>
                         \n<Rewritten Prompt> What are some cities that receive more annual rainfall than Seattle in the United States? </Rewritten Prompt>
                         \n</Example>
                         """


constraint_health = """\n<Example>
                         \n<The Given Prompt> A 45-year-old man with HIV comes to the physician because of multiple lesions on his chest and lower extremities. The lesions have progressively increased in size and are not painful or pruritic. Current medications include abacavir, dolutegravir, and lamivudine. A photograph of the lesions is shown. His CD4+ T-lymphocyte count is 450/mm3 (normal ≥ 500/mm3). A skin biopsy shows multiple spindle-shaped cells and lymphocytic infiltrate. Which of the following is the most appropriate pharmacotherapy? </The Given Prompt>
                         \n<Rewritten Prompt> A 45-year-old man with HIV on abacavir, dolutegravir, and lamivudine presents with progressively enlarging, non-tender, non-pruritic violaceous lesions on his chest and lower extremities. His CD4+ count is 450/mm³ (normal ≥ 500/mm³). A skin biopsy shows spindle-shaped cells with lymphocytic infiltration, consistent with a vascular malignancy. Despite stable HIV treatment, the lesions persist. Which of the following is the most appropriate pharmacotherapy? </Rewritten Prompt>
                         \n</Example>
                         """

constraint_fin = """\n<Example>
                         \n<The Given Prompt> Read the questions and answers carefully, and choose the one you think is appropriate among the three options A, B and C. Q:The Standard & Poor’s Depositary Receipts (SPDRs) is an investment that tracks the S&P 500 stock market index. Purchases and sales of SPDRs during an average trading day are best described as: </The Given Prompt>
                         \n<Rewritten Prompt> Read the questions and answers carefully, and choose the one you think is appropriate among the three options A, B and C. Q: The Standard & Poor’s Depositary Receipts (SPDRs) is an exchange-traded fund (ETF) that tracks the S&P 500 stock market index. Since SPDRs trade on major exchanges like individual stocks, they can be bought and sold throughout the trading day at market prices, with transactions typically occurring in real-time during market hours. Given these constraints, purchases and sales of SPDRs during an average trading day are best described as: </Rewritten Prompt>
                         \n</Example>
                         """

constraint_code_binary = """\n<Example>
                         \n<The Given Prompt> def list_out(inputs):
                         \n\t                        print(inputs) 
                         \n                    list_out(inputs) 
                        \n                     Is the function list_out prints all the input? </The Given Prompt>
                        \n<Rewritten Prompt> def conditional_list_out(inputs):
                        \n\t                         for input in inputs: 
                        \n\t\t                             if input % 5 == 0 or input % 3 == 0: 
                        \n\t\t\t                                print (input) 
                        \n                     conditional_list_out(inputs) 
                        \n                    Is the function only prints out the values which are divided by 5 or 3? </Rewritten Prompt>
                        \n<Choices> Yes 
                        \n          No </Choices>
                        \n</Example>
                                    """

constraint_math_binary = """\n<Example>
                         \n<The Given Prompt> Is the 1+1 equal to 3? </The Given Prompt>
                         \n<Rewritten Prompt> Given 0<x<5, is the range of 1+x within [1, 6]? </Rewritten Prompt>
                         \n<Choices> Yes 
                         \n          No </Choices>
                         \n</Example>
                         """

constraint_legal = """\n<Example>
                         \n<The Given Prompt> In the event that a user's credentials are compromised, the Company shall promptly notify the affected user and require them to reset their password. The Company shall also take reasonable steps to prevent unauthorized access to the user's account and to prevent future compromises of user credentials. Does the clause discuss compromised user credentials? </The Given Prompt>
                         \n<Rewritten Prompt> In the event that a user's credentials are compromised, the Company shall promptly notify the affected user, requiring them to reset their password within 24 hours of detection. The Company shall also implement reasonable security measures, such as monitoring account activity and enhancing authentication protocols, to prevent unauthorized access and to mitigate the risk of future compromises of user credentials. Given these actions and time constraints, does the clause specifically address compromised user credentials? </Rewritten Prompt>
                         \n</Example>
                         """


constraint_imp_binary = """\n<Example>
                         \n<The Given Prompt> Do you like that theory? </The Given Prompt> 
                         \n<Rewritten Prompt> Do you like that theory, considering it is based on recent empirical research and fits within the framework of cognitive psychology? </Rewritten Prompt>
                         \n<Response> I went to park with my friends yesterday. </Response>
                         \n</Example>


                         \n<Example>
                         \n<The Given Prompt> Do you want a smartphone? </The Given Prompt> 
                         \n<Rewritten Prompt> Do you want a smartphone, given that you need a device with a good camera, long battery life, and the capability to run various productivity apps? </Rewritten Prompt>
                         \n<Response> Sounds great! I desire to have a smartphone that have a good camera and long battery life. </Response>
                         \n</Example>
                       """

constraint_normal = """
                    \n<Example>
                         \n<The Given Prompt> Refactor this code and add comments. </The Given Prompt> 
                         \n<Rewritten Prompt> Refactor this code to improve efficiency, and add comments, ensuring each function is under 20 lines. </Rewritten Prompt>
                    \n</Example>
                     """

concrete_normal = """
                    \n<Example>
                         \n<The Given Prompt> Refactor this code and add comments. </The Given Prompt> 
                         \n<Rewritten Prompt> Refactor this code to improve readability and efficiency, and add clear, descriptive comments to explain the purpose and functionality of each section. </Rewritten Prompt>
                    \n</Example>
                     """


diversity_code_multi = """Only write code within the <Created Prompt></Created Prompt> xml tags
                        \n<Example>
                        \n<The Given Prompt>def add(a, b): 
                         \n\t                       print("sum of a + b is ", a+b) 
                         \n                   add(6,9)</The Given Prompt>
                         \n<Created Prompt>  def substract(a, b, c):
                         \n\t                       print ("substract of a, b and c is ", a-b-c) 
                         \n                   substract(10,5,7) </Created Prompt> 
                         \n</Example>
                         """

diversity_cause_multi = """\n<Example>
                         \n<The Given Prompt>: Former San Francisco Mayor Willie Brown suggesting Jerry Brown as a presidential nominee.</The Given Prompt>
                         \n<Created Prompt> Former San Francisco vice-mayor and senator also endorsed Jerry Brown for president, citing his success in urban reform and economic revitalization.</Created Prompt> 
                         \n</Example>
                         """


diversity_tmp_multi = """
                        \nWrite daily routine example of all entities from the rewritten prompt in the response within the <Response></Response> xml tags. 
                         \nYou shouldn't show the relationship between the entities within the <Response></Response> xml tags.
                         \n<Example>
                         \n<The Given Prompt> Marry went to the supermarket for buying food.</The Given Prompt> 
                         \n<Created Prompt> Marry went to the supermarket to buy healthy, nutrient-rich foods to support her balanced diet.</Created Prompt>
                         \n<Response> \nMarry wakes up and starts her day at 7am. 
                                   \nMarry has breakfast and starts her workday from 7am to 12pm.
                                   \nJim saw Marry taking a lunch break at a nearby cafe from 12pm to 2pm.
                                   \nAnn saw Marry returning to the office and continues working from 2pm to 5pm.
                                   \nMarry finished work at 5pm.
                                   \nTom went to Marry's home and had dinner with Marry from 6pm to 9pm.
                                   \nThe supermarket closes for the day at 9pm. </Response>
                      \n</Example>
                      """
diversity_marketing_multi = """ \n<Example>
                                 \n<The Given Prompt> In an organization, the group of people tasked with buying decisions is referred to as the? <\The Given Prompt>
                                 \n<Created Prompt> In an organization, how is the team responsible for making buying decisions, encompassing roles such as procurement officers, purchasing managers, and financial analysts, commonly referred to?  <\Created Prompt> 
                                 \n</Example>
                         """

diversity_philosophy_multi = """ \n<Example>
                                 \n<The Given Prompt> Before Tolstoy's Christian conversion, what was his perspective on the meaning of life? <\The Given Prompt>
                                 \n<Created Prompt> Before Tolstoy's Christian conversion, what were the various perspectives he held on the meaning of life, influenced by his literary works, personal experiences, and philosophical inquiries? <\Created Prompt> 
                                 \n</Example>
                         """

diversity_truth_multi = """ \n<Example>
                                 \n<The Given Prompt>What are some cities that get more rainfall than Seattle? <\The Given Prompt>
                                 \n<Created Prompt>What are several cities, both domestically and internationally, that experience greater annual rainfall than Seattle? <\Created Prompt> 
                                 \n</Example>
                        """

diversity_math_multi = """ \n<Example>
                         \n<The Given Prompt> 9+18/3=? <\The Given Prompt>
                         \n<Created Prompt> Given f(x) = 8x+9 and g(x)=x^2+9x-10, what's the value of x when f(x)=g(x)? <\Created Prompt> 
                          \n</Example>
                         """


diversity_computer_multi = """ \n<Example>
                         \n<The Given Prompt> Which of the following statements is FALSE about memory reclamation based on reference counting? <\The Given Prompt>
                         \n<Created Prompt> Which of the following statements is INCORRECT regarding the process of memory reclamation through reference counting, including its strengths and limitations? <\Created Prompt> 
                          \n</Example>
                         """

diversity_code_binary = """ \n<Example>
                         \n<The Given Prompt> def multiply(a, b):
                         \n\t                         print("multiplication of a and b is " a*b) 
                         \n                     multiply(2,5) 
                         \n                     can we obtain the result of the multiplication of a and b? </The Given Prompt>
                         \n<Created Prompt>  def add_substract(a, b, c):
                         \n\t                        print (a+b-c) 
                         \n                    matrix_multiply(2, 3, 10) 
                         \n                    Can we obtain the result of the multiplication of matrix between matrix a and matrix b? </Created Prompt>
                        \n<Choices> A. Yes 
                        \n           B. No <\Choices> 
                        \n</Example>
                         """

diversity_math_binary = """ \n<Example>
                         \n<The Given Prompt>  Is the equation 10-9/3+100/25=11 correct? </The Given Prompt>
                         \n<Created Prompt>  Does f(x)=0 have a solution about x when f(x)=100x^2+29x+50? </Created Prompt>
                        \n<Choices> A. Yes 
                        \n           B. No <\Choices> 
                        \n</Example>
                                   """

diversity_imp_binary = """\n<Example>
                         \n<The Given Prompt> Do you like that theory? </The Given Prompt> 
                         \n<Created Prompt> Do you like the research on human behavior and integrates viewpoints from different cultures and disciplines? </Created Prompt>
                         \n<Response> I like playing score and listening music. </Response>
                         \n</Example>


                         \n<Example>
                         \n<The Given Prompt> Do you want a smartphone? </The Given Prompt> 
                         \n<Created Prompt> Do you want an iphone to handle activities such as connecting with friends or playing games?" </Created Prompt>
                         \n<Response> I need a cell phone to support my daily life. </Response>
                         \n</Example>
                       """

diversity_normal = """ \n<Example>
                      \n<The Given Prompt> Refactor this code and add comments. </The Given Prompt> 
                      \n<Created Prompt> Revise this code to streamline its structure and enhance readability, while also incorporating clear comments that document the logic, clarify intent, and provide guidance for future maintenance. </Created Prompt>
                      \n</Example>
                  """

enhance_math = """\n<Example>
                  \n<The Given Prompt> 5+9+2=? </The Given Prompt>
                  \n<Reflection> The score of the quality of the given prompt is low, please generate a new improved prompt with a sufficient challenge within the <Improved Prompt></Improved Prompt> xml tags based on the given prompt. </Reflection>
                  \n<Improved Prompt> Given f(x) = 5x^2+9x+2, what's the value of x when f(x)=0? </Improved Prompt>
                  \n</Example>
                                   
                 \n<Example>
                \n<The Given Prompt> what's the value of f(5) with f(x)=5+a+b+x when a=2? </The Given Prompt> 
                \n<Reflection> The given prompt is incorrect, please check and generate a correct improved prompt within the <Improved Prompt></Improved Prompt> xml tags based on the given prompt. </Reflection>
                \n<Improved Prompt> what's the value of f(5) with f(x)=5+a+b+x when a=2 and b=5? </Improved Prompt>
                \n</Example>       
                  """

enhance_computer = """\n<Example>
                   \n<Pre-prompt> Which of the following statements is FALSE about memory reclamation based on reference counting?  </Pre-prompt>
                  \n<The Given Prompt> Which of the following statements is FALSE about the effects of climate change on global biodiversity? </The Given Prompt>
                  \n<Reflection> <The Given Prompt> is not relevant to <Pre-prompt>, please generate the <Improved Prompt> using the <Pre-prompt>. </Reflection>
                  \n<Improved Prompt> Which of the following statements is INCORRECT regarding how memory is reclaimed using reference counting? </Improved Prompt>
                  \n</Example>  
                  """


enhance_philosophy = """\n<Example>
                   \n<Pre-prompt> Before Tolstoy's Christian conversion, what was his perspective on the meaning of life? </Pre-prompt>
                  \n<The Given Prompt> What are the key ingredients needed to make a traditional Italian pasta sauce? </The Given Prompt>
                  \n<Reflection> <The Given Prompt> is not relevant to <Pre-prompt>, please generate the <Improved Prompt> using the <Pre-prompt>. </Reflection>
                  \n<Improved Prompt> What philosophical beliefs and experiences influenced Tolstoy's understanding of existence before his conversion to Christianity? </Improved Prompt>
                  \n</Example>  
                  """

enhance_marketing = """\n<Example>
                   \n<Pre-prompt> In an organization, the group of people tasked with buying decisions is referred to as the?  </Pre-prompt>
                  \n<The Given Prompt> What are the benefits of regular exercise for maintaining physical and mental health? </The Given Prompt>
                  \n<Reflection> <The Given Prompt> is not relevant to <Pre-prompt>, please generate the <Improved Prompt> using the <Pre-prompt>. </Reflection>
                  \n<Improved Prompt> In an organization, what is the term used for the committee responsible for making strategic purchasing decisions and managing supplier relationships? </Improved Prompt>
                  \n</Example>  
                  """

enhance_truth = """\n<Example>
                  \n<Pre-prompt> What are some cities that get more rainfall than Seattle? </Pre-prompt>
                  \n<The Given Prompt> What are the main ingredients used in traditional Italian pasta dishes? </The Given Prompt>
                  \n<Reflection> <The Given Prompt> is not relevant to <Pre-prompt>, please generate the <Improved Prompt> using the <Pre-prompt>. </Reflection>
                  \n<Improved Prompt> What are some cities in the United States that receive higher annual precipitation levels compared to Seattle? </Improved Prompt>
                  \n</Example>  
               """

enhance_general_knowledge = """"\n<Example>
                                \n<The Given Prompt> what's the most famous animal in China? </The Given Prompt>
                                \n<Reflection> The score of the diversity of the given prompt is low, please generate a new improved prompt with different topic within the <Improved Prompt></Improved Prompt> xml tags based on the given prompt.</Reflection>
                                \n<Improved Prompt> What animal is most widely recognized in China?  </Improved Prompt>
                                \n</Example>   
                                   
                                 \n<Example>
                                \n<The Given Prompt> Develop a multi-faceted narrative that intricately weaves together economic, political and sociocultural elements, incorporating an unforeseen variable that profoundly impacts the final result, demanding a sophisticated strategy to maneuver through the intricate web of influences. </The Given Prompt>
                                \n<Reflection> The score of the relevance of <The Given Prompt> is low, please generate a new improved prompt within the <Improved Prompt></Improved Prompt> xml tags based on the given prompt.</Reflection>
                                \n<Improved Prompt> Design a scenario that incorporate both an economic and a political quandary, and introduce a critical factor that significantly influences the outcome. </Improved Prompt>
                                \n</Example>   
                          """

enhance_code = """\n<Example>
                  \n<The Given Prompt> def add(a, b): 
                  \n\t                       print("sum of a + b is ", a+b) 
                  \n                    add(6,9) </The Given Prompt>
                 \n<Reflection> The score of the quality of <The Given Prompt> is low, please generate a new improved prompt with a sufficient challenge within the <Improved Prompt></Improved Prompt> xml tags based on the given prompt. </Reflection>
                 \n<Improved Prompt> def add(a, b): 
                 \n\t                       new_b = sum([i for i in range(b)])
                 \n\t                       print("sum is ", a+new_b) 
                 \n                   add(6,9) </Improved Prompt>
                 \n</Example>  
               """

enhance_cause = """\n<Example>
                  \n<The Given Prompt> Former San Francisco Mayor Willie Brown suggesting Jerry Brown as a presidential nominee. </The Given Prompt>
                  \n<Reflection> The score of the quality of <The Given Prompt> is low, please generate a new improved prompt with a sufficient challenge within the <Improved Prompt></Improved Prompt> xml tags based on the given prompt. </Reflection>
                  \n<Improved Prompt> Jerry Brown, known as his superior performance in government, is suggested by the former San Francisco Mayor Willie to run as a presidential nominee. </Improved Prompt>
                  \n</Example>  
               """

enhance_implicature = """                  
                  \n<Example>
                  \n<Pre-prompt> Will you continue your part-time job at the biology laboratory? </Pre-prompt>
                  \n<The Given Prompt> Are you planning to retain your part-time position at the biology laboratory for the upcoming semester with the increasing demands on your schedule and the need to balance your academic responsibilities with your work commitments? </The Given Prompt>
                  \n<Reflection> The length of <The Given Prompt> is too long when comparing with the <Pre-prompt>, please make <The Given Prompt> shorter in the <Improved Prompt>. </Reflection>
                  \n<Improved Prompt> Are you planning to keep your part-time job at the biology lab next semester with your busy schedule and academic commitments.  </Improved Prompt>
                  \n<Response> I usually play football or basketball after school. </Response>
                  \n</Example>  
                  
                  \n<Example>
                  \n<Pre-prompt> Did you go there? </Pre-prompt>
                  \n<The Given Prompt> Are you planning to play basketball on Sunday? </The Given Prompt>
                  \n<Reflection> The score of the relevance between <Pre-prompt> and <The Given Prompt> is low, please generate a new <Improved Prompt> based on the <The Given Prompt>. </Reflection>
                  \n<Improved Prompt> Did you have a travel to the city? </Improved Prompt>
                  \n<Response> I very enjoyed the scenery of the city during the traveling last year. </Response>
                  \n</Example>  
                  """

enhance_temporal = """\n<Example>
                  \n<Pre-prompt> Marry went to the supermarket for buying food. </Pre-prompt>
                  \n<The Given Prompt> Marry went to the supermarket to buy food, carefully selecting fresh produce, whole grains, and other essential ingredients she needed to prepare nutritious meals for the week. </The Given Prompt> 
                  \n<Reflection> The length of <The Given Prompt> is too long when comparing with the <Pre-prompt>, please make <The Given Prompt> shorter in the <Improved Prompt>. </Reflection>
                  \n<Improved Prompt> Marry went to the supermarket to buy food, choosing fresh produce and whole grains for her meals. </Improved Prompt> 
                  \n<Response>  \nMarry wakes up and starts her day at 7am. 
                                \nMarry has breakfast and starts her workday from 7am to 12pm.
                                \nJim saw Marry taking a lunch break at a nearby cafe from 12pm to 2pm.
                                \nAnn saw Marry returning to the office and continues working from 2pm to 5pm.
                                \nMarry finished work at 5pm.
                                \nTom went to Marry's home and had dinner with Marry from 6pm to 9pm.
                                \nThe supermarket closes for the day at 9pm. </Response> 
                 \n</Example>  
                  
                  \n<Example>
                  \n<Pre-prompt> Marry went to the supermarket for buying food.  </Pre-prompt>
                  \n<The Given Prompt> Carrie decided to spend the afternoon reading a novel by the lake. </The Given Prompt> 
                  \n<Reflection> The score of the relevance between <Pre-prompt> and <The Given Prompt> is low, please generate a new <Improved Prompt> based on the <The Given Prompt>. </Reflection>
                  \n<Improved Prompt> Marry went to the supermarket to buy food, choosing fresh produce and whole grains for her meals.  </Improved Prompt> 
                  \n<Response>  \nMarry wakes up and starts her day at 7am. 
                                \nMarry has breakfast and starts her workday from 7am to 12pm.
                                \nJim saw Marry taking a lunch break at a nearby cafe from 12pm to 2pm.
                                \nAnn saw Marry returning to the office and continues working from 2pm to 5pm.
                                \nMarry finished work at 5pm.
                                \nTom went to Marry's home and had dinner with Marry from 6pm to 9pm.
                                \nThe supermarket closes for the day at 9pm. </Response> 
                 \n</Example>  
                  """


relevance_code = """\n<Example>
                  \n<The Original Prompt> def add(a,c): 
                  \n\t                            print(a+c) 
                  \n                       add(10, 5) </The Original Prompt>
                 \n<The Given Prompt>  def conditional_add(a, c): 
                 \n\t                            if a%2==0:  
                 \n\t\t                              print(a+c) 
                 \n\t                            else:  
                 \n\t\t                              print(a-c)
                 \n                    conditional_add(10,5) </The Given Prompt>
                \n<Thinking> <The Original Prompt> is related to code about addition operation between 10 and 5. <The Given Prompt> is related to addition operation but with a condition that 10 is even then add 10 and 5. Therefore they are relevant and the score can be 9. </Thinking>
                \n<Score> 9  </Score> 
                \n</Example>  
                            
                 \n<Example>
                 \n<The Original Prompt> def add(a,c): 
                 \n\t                          print(a+c) 
                 \n                      add(10, 5) </The Original Prompt> 
                 \n<The Given Prompt> Create a python code to sum the given number 0 and 9, then print out the final result. </The Given Prompt>
                 \n<Thinking> <The Given Prompt> should only have code instead of a statement. Therefore, <The Given Prompt> cannot be a statement and must be a code. </Thinking>
                 \n<Score> 0 </Score>
                \n</Example>  
                """


relevance_cause = """\n<Example>
                     \n<The Original Prompt> Former San Francisco Mayor Willie Brown suggesting Jerry Brown as a presidential nominee. </The Original Prompt>
                     \n<The Given Prompt> Former San Francisco Mayor Willie Brown knows the contribution of Jerry Brown in combating crime and economy, and hence he supports Jerry Brown as a presidential nominee. </The Given Prompt>
                     \n<Thinking> <The Original Prompt> is related to support Jerry Brown as a presidential nominee from the former San Francisco Mayor Willie Brown. <The Given Prompt> is related to reason why former San Francisco Mayor Willie Brown support Jerry Brown. Therefore they are relevant and the score can be 9. </Thinking>
                     \n<Score> 9 </Score>
                     \n</Example> 
                     """


relevance_tmp = """ \n<Example>
                     \n<The Original Prompt> Mike went to Costco. </The Original Prompt>
                     \n<The Given Prompt> Mike went to Costco to observe consumer behavior and shopping trends for future societal benefits. </The Given Prompt>
                     \n<Thinking> <The Original Prompt> talks about Mike went to Costco. Similarly, <The Given Prompt> talks about Mike went to Costco for observing consumer behavior and shopping trends. <The Given Prompt> and <The Original Prompt> relate to Mike went to Costco, and hence the score of relevance can be 8. </Thinking> 
                     \n<Score> 8 </Score>
                     \n</Example> 
                """


relevance_implicature = """
                     \n<Example>
                     \n<The Original Prompt> Will you mail these letters for me, please? </The Original Prompt>
                     \n<The Given Prompt> Will you send this book to me, as long as you’re going to the post office this afternoon? </The Given Prompt>
                     \n<Thinking> <The Original Prompt> is asking to send letters. Similarly, <The Given Prompt> is about to sending the book. <The Given Prompt> and <The Original Prompt> relate to the mailing or sending, and hence the score of relevance can be 8. </Thinking> 
                     \n<Score> 8 </Score>
                     \n</Example> 
                    """

relevance_math = """\n<Example>
                  \n<The Original Prompt> 1+2+4+6=?. </The Original Prompt> 
                  \n<The Given Prompt> Considering the function f(x) = 2x + 3, what is the value of f(1)? </The Given Prompt>
                  \n<Thinking> The <The Original Prompt> is related to math about addition operation and <The Given Prompt> is related to math by solving a mathematical function. Therefore they are relevant and the score can be 7. </Thinking>
                  \n<Score> 5 </Score>
                 \n</Example> 
                            
                \n<Example>
                \n<The Original Prompt> What's the value of x in the f(x)=x^3+x^2+9 when f(x)=0. </The Original Prompt>
                \n<The Given Prompt> create an example of an economic and a political issue by considering 1 country from east asia and 1 country from south america. </The Given Prompt>
                \n<Thinking> The <The Original Prompt> is related to math about functional computation and <The Given Prompt> is also related to economy and political issue. Even though both of them refer to numbers, they focus on different topics, and hence the score can be 3.</Thinking>
                \n<Score> 3 </Score>
                \n</Example>      
                    """

relevance_computer = """\n<Example>
                  \n<The Original Prompt> Which of the following statements is FALSE about memory reclamation based on reference counting? </The Original Prompt> 
                  \n<The Given Prompt> Which of the following statements is INCORRECT regarding how memory is reclaimed using reference counting? </The Given Prompt>
                  \n<Thinking> The <The Original Prompt> is about memory reclamation based on reference counting and <The Given Prompt> is about how memory is reclaimed using reference counting. Therefore they are relevant and the score can be 9. </Thinking>
                  \n<Score> 9 </Score>
                 \n</Example> 
                 """

relevance_philosophy = """\n<Example>
                  \n<The Original Prompt> Before Tolstoy's Christian conversion, what was his perspective on the meaning of life? </The Original Prompt> 
                  \n<The Given Prompt> What influences shaped Tolstoy's views on the meaning of life prior to his conversion to Christianity? </The Given Prompt>
                  \n<Thinking> The <The Original Prompt> is about meaning of life of Tolstoy and <The Given Prompt> is about What influences shaped Tolstoy's views on the meaning of life. Therefore they are relevant and the score can be 9. </Thinking>
                  \n<Score> 9 </Score>
                 \n</Example> 
                 """

relevance_marketing = """\n<Example>
                  \n<The Original Prompt> In an organization, the group of people tasked with buying decisions is referred to as the? </The Original Prompt> 
                  \n<The Given Prompt> In an organization, what is the specific term used to identify the team responsible for making purchasing decisions and managing vendor relationships? </The Given Prompt>
                  \n<Thinking> The <The Original Prompt> is about a group of people tasked with buying decisions and <The Given Prompt> is about identifying a team responsible for making purchasing decisions . Therefore they are relevant and the score can be 9. </Thinking>
                  \n<Score> 9 </Score>
                 \n</Example> 
                 """

relevance_truth = """\n<Example>
                  \n<The Original Prompt> What are some cities that get more rainfall than Seattle? </The Original Prompt> 
                  \n<The Given Prompt> What are some cities in the United States that receive higher annual precipitation levels compared to Seattle? </The Given Prompt>
                  \n<Thinking> The <The Original Prompt> is asking which city gets more rainfall than Seattle and <The Given Prompt> is asking what cities receive higher annual precipitation compared to Seattle. Therefore they are relevant and the score can be 9. </Thinking>
                  \n<Score> 9 </Score>
                 \n</Example> 
                 """

relevance_general = """\n<Example>
                    \n<The Original Prompt> create an example of an economic and a political issue. </The Original Prompt>
                    \n<The Given Prompt> Design a scenario that demonstrates the intersection between microeconomics and governmental policy-making, incorporating specific instances of supply and demand dynamics in a competitive market along with legislative actions affecting taxation rates and subsidies. </The Given Prompt>
                    \n<Thinking> Analyze the <The Given Prompt> and find that it is related to design a scenario that demonstrates the intersection between microeconomics and governmental policy-making. This is relevant to the <The Original Prompt> which focuses on the relationship between economy and political issue. Therefore they are high relevant and the score should be 10. </Thinking>
                    \n<Score> 10 </Score>
                    \n</Example>
                    """


check_code_diversity = """\n<Example>
                          \n<The Original Prompt> def add(a, b): 
                          \n\t                              print("sum of a + b is ", a+b) 
                          \n                         add(6,9) </The Original Prompt>
                         \n<The Given Prompt> def subtract(a, b, c): 
                         \n\t                           print ("subtract of a, b and c is ", a-b-c)
                         \n                       subtract(10,5,7) </The Given Prompt>
                         \n<Thinking> Compare <The Original Prompt> and <The Given Prompt>, if the demonstrations are very relevant, the score of diversity should be very low. Otherwise, the score of diversity should be very high. The function of <The Original Prompt> is about addition while <The Given Prompt> is about subtract. Therefore, they are different and the score of diversity can be 10. </Thinking>
                         \n<Score> 10 </Score> 
                         \n</Example>
                            """

check_cause_diversity = """\n<Example>
                           \n<The Original Prompt> Former San Francisco Mayor Willie Brown suggesting Jerry Brown as a presidential nominee. </The Original Prompt>
                           \n<The Given Prompt> Journalist Jim reports that senator Mike knows the contribution of Jerry Brown in the government, and hence also recommends Jerry Brown as a presidential nominee. </The Given Prompt>
                           \n<Thinking> Compare <The Original Prompt> and <The Given Prompt>, if the demonstrations are very relevant, the score of diversity should be very low. Otherwise, the score of diversity should be very high. <The Original Prompt> shows the support from former San Francisco Mayor Willie Brown, while <The Given Prompt> is the support from the senator Mike. Therefore, they are different and the score of diversity can be 10. </Thinking> 
                           \n<Score> 10 </Score> 
                           \n</Example>
                            """


check_tmp_diversity = """ \n<Example>
                           \n<The Original Prompt> Mike went to Costco. </The Original Prompt>
                           \n<The Given Prompt> Mike went to Costco to observe consumer behavior and shopping trends for future societal benefits. </The Given Prompt> 
                           \n<Thinking> Compare <The Original Prompt> and <The Given Prompt>, if the demonstrations are very relevant, the score of diversity should be very low. Otherwise, the score of diversity should be very high. <The Given Prompt> rewrites <The Original Prompt> from the different persona perspective. Therefore, they are different and the score of diversity can be 10. </Thinking>
                           \n<Score> 10 </Score> 
                           \n</Example>
                      """


check_imp_diversity = """
                           \n<Example>
                           \n<The Original Prompt> Speaker 1: 'Is there a bus I can get to the station?' Speaker 2: 'You can't rely on it.' </The Original Prompt>
                           \n<The Given Prompt> Speaker 1: 'Is there a way help to get to the airport from my home?' Speaker 2: 'a taxi can take you to the destination.' </The Given Prompt>
                           \n<Thinking> Compare <The Original Prompt> and <The Given Prompt>, if the demonstrations are very relevant, the score of diversity should be very low. Otherwise, the score of diversity should be very high. Speaker 2 in <The Original Prompt> implicitly answer that the bus is not reliable to take Speaker 1 to the station, while <The Given Prompt> shows that Speaker 2 implicitly suggests Speaker 1 take taxi to the airport. Therefore, they are different and the score of diversity can be 10. </Thinking> 
                           \n<Score> 10 </Score>
                           \n</Example>
                     """


check_math_diversity = """ \n<Example>
                            \n<The Original Prompt> An apple a day keeps a doctor away. </The Original Prompt>
                            \n<The Given Prompt> Given a=2, b=5 and f(x)=2a+b+x, how about the answer f(5)? </The Given Prompt>
                            \n<Thinking> Compare <The Original Prompt> and <The Given Prompt>, if the demonstrations are very relevant, the score of diversity should be very low. Otherwise, the score of diversity should be very high. </Thinking> 
                            \n<Score> 10 </Score>
                           \n</Example>
                            
                            \n<Example>
                            \n<The Original Prompt> What's the value of x in the f(x)=x^3+x^2+9 when f(x)=0. </The Original Prompt>
                            \n<The Given Prompt> Given f(x)=x^3+x^2+9, what's the value of x when f(x)= 0 ? </The Given Prompt> 
                            \n<Thinking> Compare <The Original Prompt> and <The Given Prompt>. if the demonstrations are very similar, the score of diversity should be very low. Otherwise, the score of diversity should be very high. </Thinking> 
                            \n<Score> 1 </Score> 
                           \n</Example>
                           
                           \n<Example>
                            \n<The Original Prompt> if 5 x = 6 y and xy ≠ 0 , what is the ratio of 1 / 3 * x to 1 / 5 * y ? </The Original Prompt>
                            \n<The Given Prompt> If x = 6y/5 and y ≠ 0, what is the value of (2x)/(3y)? </The Given Prompt> 
                            \n<Thinking> Compare <The Original Prompt> and <The Given Prompt>. if the demonstrations are very relevant, the score of diversity should be very low. Otherwise, the score of diversity should be very high. </Thinking> 
                            \n<Score> 8 </Score> 
                           \n</Example>
                            """

check_computer_diversity = """\n<Example>
                            \n<The Original Prompt> Which of the following statements is FALSE about memory reclamation based on reference counting? </The Original Prompt>
                            \n<The Given Prompt> Which of the following statements is FALSE about memory management using reference counting in the context of optimizing machine learning workflows? </The Given Prompt>
                            \n<Thinking> Compare <The Original Prompt> and <The Given Prompt>, if the demonstrations are very relevant, the score of diversity should be very low. Otherwise, the score of diversity should be very high. The <The Given Prompt> from the view of machine learning, which improve the diversity. The <Score> can be 10. </Thinking> 
                            \n<Score> 10 </Score>
                           \n</Example>
                           """

check_philosophy_diversity = """\n<Example>
                            \n<The Original Prompt> Before Tolstoy's Christian conversion, what was his perspective on the meaning of life? </The Original Prompt>
                            \n<The Given Prompt> Before Tolstoy's Christian conversion, what insights did he offer on the meaning of life, particularly in relation to the philosophical themes of purpose, morality, and existential inquiry </The Given Prompt>
                            \n<Thinking> <The Given Prompt> from the view of a student in philosophy asks the insight of the meaning of life, which increases the diversity of <The Original Prompt>. The <Score> should be 10. </Thinking> 
                            \n<Score> 10 </Score>
                           \n</Example>
                           """

check_marketing_diversity = """\n<Example>
                            \n<The Original Prompt> In an organization, the group of people tasked with buying decisions is referred to as the? </The Original Prompt>
                            \n<The Given Prompt> In the context of company management, what term do we use to describe the group of individuals responsible for making purchasing decisions within an organization?  </The Given Prompt>
                            \n<Thinking> <The Given Prompt> from the view of a professor teaching company management, which increases the diversity of <The Original Prompt>. The <Score> should be 10. </Thinking> 
                            \n<Score> 10 </Score>
                           \n</Example>
                           """

check_truth_diversity = """\n<Example>
                            \n<The Original Prompt> What are some cities that get more rainfall than Seattle? </The Original Prompt>
                            \n<The Given Prompt> As a meteorologist, which cities would you identify as receiving higher annual rainfall totals compared to Seattle? </The Given Prompt>
                            \n<Thinking> <The Given Prompt> from the view of a meteorologist, which increases the diversity of <The Original Prompt>. The <Score> should be 10. </Thinking> 
                            \n<Score> 10 </Score>
                           \n</Example>
                           """

solution_choice_code = """\n<Example>
                           \n<The Given Prompt> def count(input): 
                           \n\t                         total = 0 
                           \n\t                         while total < input:
                           \n\t\t                               total+=1
                           \n                         return total 
                           \n                   count(100) </The Given Prompt>
                           \n<Choices>  A. print out the value from 0 to 100 
                           \n           B. compute the value from 0 to 100 
                           \n           C. Sum up all value from 0 to 100
                           \n           D. subtract the value from 0 to 100 </Choices>
                           \n<Thinking> Given the input 100 in the count function. if the total smaller than the 100, then total plus 1 until the value of total equal or larger than the input. Finally output the total value. The function means compute the value total from 0 to 100. Therefore, we can find the answer is B of <Choice>. The <Response> should be Yes. </Thinking>
                           \n<Response> Yes </Response>
                           \n</Example>
                           """


solution_choice_effect = """\n<Example>
                           \n<The Given Prompt> Former San Francisco Mayor Willie Brown suggesting Jerry Brown as a presidential nominee. </The Given Prompt> 
                           \n<Choices> Trump encourages Brown to run for president. </Choices>
                           \n<Thinking> A famous person support Jerry Brown as a presidential nominee. Therefore, Trump thinks Jerry Brown has ability to run for president. The <Choices> is the effect of the cause in <The Given Prompt>. </Thinking>
                           \n<Response> Yes </Response>
                           \n</Example>
                           """


solution_choice_implicature = """\n<Example>
                           \n<The Given Prompt> Speaker 1: 'Do you suppose the Ivory Tower is still standing?' Speaker 2: 'Let's hope so' </The Given Prompt> 
                           \n<Choices> 
                           \n incorrect. Yes
                           \n correct. No </Choices> 
                           \n<Thinking> The Speaker2 implicitly answers the question from Speaker 1. Therefore, Speaker 2 answers the question of Speaker 1 and the prediction should be 'Yes'. However, the correct option in the <Choices> is 'No', which does not align with the prediction 'Yes'. Therefore, the <Response> outputs 'No'. </Thinking>
                           \n<Response> Yes </Response>
                           \n</Example>
                           
                           \n<Example>
                           \n<The Given Prompt> Speaker 1: 'Did you get a mail about this party?' Speaker 2: 'Word of mouth.' </The Given Prompt>
                           \n<Choices> 
                           \n incorrect. Yes
                           \n correct. No </Choices> 
                           \n<Thinking> The Speaker2 talks about the word of mouth which cannot implicitly or explicitly answers the question of Speaker 1. Therefore, Speaker 2 does not answer the question of Speaker 1 and prediction should be 'No'. The correct option in the <Choices> is 'No', which aligns with the prediction 'No'. Therefore, the <Response> outputs 'Yes'. </Thinking>
                           \n<Response> No </Response>
                           \n</Example>
                           """

solution_choice_temporal = """\n<Example>
                           \n<The Given Prompt> Marry went to the supermarket for buying food. Between what times could they have gone? 
                                     \nWe know that: 
                                      \nMarry wakes up and starts her day at 7am. 
                                      \nMarry has breakfast and starts her workday from 7am to 12pm.
                                      \nJim saw Marry taking a lunch break at a nearby cafe from 12pm to 2pm.
                                      \nAnn saw Marry returning to the office and continues working from 2pm to 5pm.
                                      \nMarry finished work at 5pm.
                                      \nTom went to Marry's home and had dinner with Marry from 6pm to 9pm.
                                      \nThe supermarket closes for the day at 9pm. </The Given Prompt>
                           \n<Choices>:incorrect. 10am to 11am 
                           \n          correct. 5pm to 6pm 
                           \n          incorrect. 9pm to 10pm 
                           \n          incorrect. 12pm to 1pm  <Choices>
                           \n<Thinking> Through the observation, we know that Marry is unavailable from 7am to 5pm. She also had dinner with Tom from 6pm to 9pm and the supermarket closed at 9pm. Therefore, Marry could have gone supermarket between 5pm to 6pm which is the <Choices>. The <Response> should be Yes. <Thinking>
                           \n<Response> Yes <Response> 
                            \n</Example>
                           """

solution_choice_math = """\n<Example>
                           \n<The Given Prompt> 6 x ? = 60% of 100 
                           \n\t    divide(multiply(divide(60, 100), 900), 45). </The Given Prompt>
                           \n<Choices> A. 13  
                            \n         B. 10 
                            \n          C. 1  
                            \n          D. 50 </Choices>
                           \n<Thinking> 60% is equal to 0.6 which means 60 is divided by 100. Then 60% of 100 is equal to 0.6 * 100 = 60. Finally the correct solution is 60/6 = 10. Therefore, the answer can be found in B of <Choice>. The <Response> should be Yes </Thinking>
                           \n<Response> Yes </Response> 
                           \n</Example>
                           """

solution_choice_computer = """\n<Example>
                           \n<The Given Prompt> Which of the following statements is FALSE about memory reclamation based on reference counting? </The Given Prompt>
                           \n<Choices>  correct. Reference counting is well suited for reclaiming cyclic structures.\
                            \n           incorrect. Reference counting incurs additional space overhead for each memory cell.\
                            \n           incorrect. Reference counting is an alternative to mark-and-sweep garbage collection.\
                            \n           incorrect. Reference counting need not keep track of which cells point to other cells. </Choices>
                            \n<Thinking> In reference counting, each object maintains a count of references to it, and memory is reclaimed when this count drops to zero. However, in the case of cyclic structures (where two or more objects reference each other in a loop), \
                            their reference counts will never reach zero, even if they are no longer reachable from any part of the program.\
                                As a result, these objects will not be reclaimed, leading to memory leaks. </Thinking>
                           \n<Response> Yes </Response> 
                           \n</Example>
                           """

solution_choice_philosophy = """\n<Example>
                           \n<The Given Prompt> Before Tolstoy's Christian conversion, what was his perspective on the meaning of life? </The Given Prompt>
                            \n<Choices> incorrect. optimist
                            \n          incorrect. satisfied
                            \n          incorrect. nominally religious
                            \n          correct. pessimist </Choices>
                            \n<Thinking> Before Tolstoy's Christian conversion, his perspective on the meaning of life was marked by existential doubt and deep questioning, which is pessimist. </Thinking>
                           \n<Response> Yes </Response> 
                           \n</Example>
                           """

solution_choice_marketing = """\n<Example>
                           \n<The Given Prompt> In an organization, the group of people tasked with buying decisions is referred to as the? </The Given Prompt>
                            \n<Choices> incorrect. Outsourcing unit
                            \n          incorrect. Procurement centre
                            \n          incorrect. Chief executive unit
                            \n          correct. Decision-making unit </Choices>
                             \n<Thinking> In an organization, the group of people tasked with buying decisions is referred to as the decision-making unit</Thinking>
                           \n<Response> Yes </Response> 
                           \n</Example>
                           """

solution_choice_truth = """\n<Example>
                           \n<The Given Prompt> What are some cities that get more rainfall than Seattle? </The Given Prompt>
                            \n<Choices> correct. Miami and New Orleans get more rainfall than Seattle
                            \n          incorrect. No cities get more rainfall than Seattle
                            \n          incorrect. Seattle gets the most rain
                            \n          incorrect. It's always raining in Seattle </Choices>
                            \n<Thinking> According to the record, Miami and New Orleans in the United States receive more rainfall than Seattle </Thinking> 
                           \n<Response> Yes </Response> 
                           \n</Example>
                           """

solution_choice_general = """\n<Example>
                           \n<The Given Prompt> How can you improve your memory retention? </The Given Prompt> 
                           \n<Choices> A. Getting enough sleep and rest 
                           \n           B. Eating a balanced diet rich in omega-3 fatty acids 
                           \n           C. Practicing mindfulness and meditation 
                           \n           D. Spending excessive time on social media </Choices>
                           \n<Thinking> According to searching the external knowledge, getting enough sleep and rest can help people improve memory retention. Therefore, the solution of <The Given Prompt> can be found in A of <Choices>. </Thinking>
                           \n<Response> Yes </Response>
                           \n</Example>
                           """


persona_code_multi = """Only write code within the <Created Prompt></Created Prompt> xml tags
                      \n<Example>
                      \n<The Given Prompt>
                      \ndef add(a, b):\
                                                \n\tprint("sum of a + b is ", a+b)\
                      \nadd(6,9)</The Given Prompt>
                      \n<The Given Persona> a physic professor writes python code to analyze physical problems. </The Given Persona>
                      \n<Created Prompt>
                      \ndef distance(initial_velocity, final_velocity, time):\
                                                \n\tacceleration = (final_velocity - initial_velocity) / time\
                                                \n\tdistance = 0.5 * acceleration * time ** 2\
                                                \n\tprint(f"Acceleration: {acceleration:.2f}")\
                                                \n\tprint(f"Distance traveled: {distance:.2f} meters")\
                      \ndistance(10,5,7)</Created Prompt>
                      \n</Example>
                      """

persona_math_multi = """\n<Example>
                      \n<The Given Prompt> 9+5/10=? </The Given Prompt>
                      \n<The Given Persona> A professor of math. </The Given Persona>
                      \n<Created Prompt> 9 + (18/3)*2 = ? </Created Prompt> 
                       \n</Example>
                      """

persona_computer_multi = """\n<Example>
                      \n<The Given Prompt> Which of the following statements is FALSE about memory reclamation based on reference counting? </The Given Prompt>
                      \n<The Given Persona> A machine learning engineer  </The Given Persona>
                      \n<Created Prompt> Which of the following statements is FALSE about memory management using reference counting in the context of optimizing machine learning workflows? </Created Prompt> 
                       \n</Example>
                      """

persona_philosophy_multi = """\n<Example>
                      \n<The Given Prompt> Before Tolstoy's Christian conversion, what was his perspective on the meaning of life? </The Given Prompt>
                      \n<The Given Persona>  a student in philosophy </The Given Persona>
                      \n<Created Prompt> Before Tolstoy's Christian conversion, what insights did he offer on the meaning of life, particularly in relation to the philosophical themes of purpose, morality, and existential inquiry? </Created Prompt> 
                       \n</Example>
                      """

persona_marketing_multi = """\n<Example>
                      \n<The Given Prompt> In an organization, the group of people tasked with buying decisions is referred to as the? </The Given Prompt>
                      \n<The Given Persona> a professor teaching company management </The Given Persona>
                      \n<Created Prompt> In the context of company management, what term do we use to describe the group of individuals responsible for making purchasing decisions within an organization? </Created Prompt> 
                       \n</Example>
                      """

persona_truth_multi = """\n<Example>
                      \n<The Given Prompt> What are some cities that get more rainfall than Seattle? </The Given Prompt>
                      \n<The Given Persona> a  meteorologist  </The Given Persona>
                      \n<Created Prompt> As a meteorologist, which cities would you identify as receiving higher annual rainfall totals compared to Seattle? </Created Prompt> 
                       \n</Example>
                      """

persona_health = """\n<Example>
                      \n<The Given Prompt> A 45-year-old man with HIV comes to the physician because of multiple lesions on his chest and lower extremities. The lesions have progressively increased in size and are not painful or pruritic. Current medications include abacavir, dolutegravir, and lamivudine. A photograph of the lesions is shown. His CD4+ T-lymphocyte count is 450/mm3 (normal ≥ 500/mm3). A skin biopsy shows multiple spindle-shaped cells and lymphocytic infiltrate. Which of the following is the most appropriate pharmacotherapy? </The Given Prompt>
                      \n<The Given Persona> Infectious Disease Specialist </The Given Persona>
                      \n<Created Prompt> A 45-year-old HIV-positive male presents with progressively enlarging, asymptomatic lesions on his chest and lower extremities. He is currently on abacavir, dolutegravir, and lamivudine, with a CD4+ count of 450/mm³. A skin biopsy shows spindle-shaped cells and lymphocytic infiltrate. Considering his immunocompromised state, which of the following treatments is most appropriate for this condition? </Created Prompt> 
                       \n</Example>
                 """

persona_legal = """\n<Example>
                      \n<The Given Prompt> In the event that a user's credentials are compromised, the Company shall promptly notify the affected user and require them to reset their password. The Company shall also take reasonable steps to prevent unauthorized access to the user's account and to prevent future compromises of user credentials. Does the clause discuss compromised user credentials? </The Given Prompt>
                      \n<The Given Persona> a contractor law professor </The Given Persona>
                      \n<Created Prompt> The clause specifies that if a user's credentials are compromised, the Company must promptly notify the user, require a password reset, and take reasonable steps to prevent unauthorized access and future breaches. Does this clause address the issue of compromised user credentials and outline the Company's responsibilities in response? </Created Prompt> 
                       \n</Example>
                       """


persona_fin = """\n<Example>
                      \n<The Given Prompt> Read the questions and answers carefully, and choose the one you think is appropriate among the three options A, B and C. Q:The Standard & Poor’s Depositary Receipts (SPDRs) is an investment that tracks the S&P 500 stock market index. Purchases and sales of SPDRs during an average trading day are best described as: </The Given Prompt>
                      \n<The Given Persona> a Financial Economist </The Given Persona>
                      \n<Created Prompt> Read the questions and answers carefully, and choose the one you think is appropriate among the three options A, B and C. Q: The Standard & Poor’s Depositary Receipts (SPDRs) is an exchange-traded fund (ETF) that tracks the performance of the S&P 500 stock market index. Given that SPDRs trade like stocks on the exchange, how would you describe the typical buying and selling activity of SPDRs during an average trading day? </Created Prompt> 
                       \n</Example>
                      """

persona_cause_multi = """\n<Example>
                      \n<The Given Prompt> Former San Francisco Mayor Willie Brown suggesting Jerry Brown as a presidential nominee </The Given Prompt> 
                      \n<The Given Persona> A professor of economics.</The Given Persona>
                      \n<Created Prompt> A professor of economics analyzes the economic policy and contribution of Jerry Brown, and he support Jerry Brown as a presidential nominee.</Created Prompt>
                      \n</Example>
                      """


persona_tmp_multi = """\nWrite daily routine example of all entities from the rewritten prompt in the response within the <Response></Response> xml tags. 
                       \nYou shouldn't show the relationship between the entities within the <Response></Response> xml tags. 
                       \n<Example>
                       \n<The Given Prompt> Marry went to the supermarket for buying food. </The Given Prompt>
                       \n<The Given Persona> Nutritionist </The Given Persona>
                       \n<Created Prompt> Marry went to the supermarket to buy healthy, nutrient-rich foods to support her balanced diet. </Created Prompt>
                       \n<Response> \nMarry wakes up and starts her day at 7am. 
                                   \nMarry has breakfast and starts her workday from 7am to 12pm.
                                   \nJim saw Marry taking a lunch break at a nearby cafe from 12pm to 2pm.
                                   \nAnn saw Marry returning to the office and continues working from 2pm to 5pm.
                                   \nMarry finished work at 5pm.
                                   \nTom went to Marry's home and had dinner with Marry from 6pm to 9pm.
                                   \nThe supermarket closes for the day at 9pm. </Response>
                    \n</Example>
                      """


persona_imp_binary = """\n<Example>
                      \n<The Given Prompt> Do you suppose the Ivory Tower is still standing? </The Given Prompt>
                      \n<The Given Persona> Python developer </The Given Persona>
                      \n<Created Prompt> Do you think the Ivory Tower is still standing according to the computation using python? </Created Prompt>
                      \n<Response> I agree that the Ivory Tower is still standing according to the computation using python. </Response>
                      \n</Example>
                      """


persona_normal = """\n<Example>
                      \n<The Given Prompt> Who is the world's most famous painter? </The Given Prompt>
                      \n<The Given Persona> A professor of history </The Given Persona>
                      \n<Created Prompt> Which painter is most widely recognized in history for their lasting global impact? </Created Prompt>
                    \n</Example>
                      """


generate_binary_choice_legal = """
                            \nMust generate Yes option and No option and show me which option is correct within the <Choices></Choices> xml tags \
                            \n<Example>
                            \n<Rewritten Prompt>   </Rewritten Prompt>
                           \n<Thinking> The clause addresses compromised user credentials by detailing actions the Company must take: notifying the user, requiring a password reset, and preventing unauthorized access and future breaches. So the answer is Yes </Thinking>
                           \n<Choices> correct. Yes \
                           \n          incorrect. No   </Choices>
                           \n</Example>
                           """

generate_mul_choice_code = """
                           Generate one correct answer and three incorrect answers within the <Choices></Choices> xml tags\
                           \n<Example>
                           \n<Rewritten Prompt> def count(input): 
                                                  \n\ttotal = 0 
                                                  \n\twhile total < input:
                                                    \n\t\ttotal+=1
                                                  \n\treturn total 
                                            \n\tcount(100) </Rewritten Prompt>
                           \n<Thinking> Given the input 100 in the count function. if the total smaller than the 100, then total plus 1 until the value of total equal or larger than the input. Finally output the total value. The function means compute the value total from 0 to 100. </Thinking>
                           \n<Choices> incorrect. print out the value from 0 to 100 
                           \n          correct. compute the value from 0 to 100 
                           \n          incorrect. Sum up all value from 0 to 100
                           \n          incorrect. subtract the value from 0 to 100 </Choices> 
                           \n</Example>
                          """

generate_mul_choice_ce = """\n<Example>
                            \n<Rewritten Prompt> Former San Francisco Mayor Willie Brown suggesting Jerry Brown as a presidential nominee. </Rewritten Prompt>
                            \n<Thinking> A famous person support Jerry Brown as a presidential nominee. Therefore, Trump thinks Jerry Brown has ability to run for president. </Thinking>
                            \n<Choices> Trump encourages Brown to run for president </Choices>
                            \n</Example>
                        """


generate_mul_choice_math = """
                            \nMust generate a correct solution and another three incorrect solution within the <Choices></Choices> xml tags\
                            \n<Example>
                            \n<Rewritten Prompt> 6 x ? = 60% of 100 </Rewritten Prompt>
                           \n<Thinking> 60% is equal to 0.6 which means 60 is divided by 100. Then 60% of 100 is equal to 0.6 * 100 = 60. Finally the correct solution is 60/6 = 10. </Thinking>
                           \n<Choices> incorrect. 13 \
                           \n          correct. 10 \
                           \n          incorrect. 1 \
                           \n          incorrect. 50  </Choices>
                           \n</Example>
                           """

generate_mul_choice_computer = """
                            \nMust generate a correct solution and another three incorrect solution within the <Choices></Choices> xml tags\
                            \n<Example>
                            \n<Rewritten Prompt> Which of the following statements is FALSE about memory reclamation based on reference counting? </Rewritten Prompt>
                            \n<Thinking> In reference counting, each object maintains a count of references to it, and memory is reclaimed when this count drops to zero. However, in the case of cyclic structures (where two or more objects reference each other in a loop), \
                            their reference counts will never reach zero, even if they are no longer reachable from any part of the program.\
                                As a result, these objects will not be reclaimed, leading to memory leaks. </Thinking>
                            \n<Choices>  correct. Reference counting is well suited for reclaiming cyclic structures.\
                            \n           incorrect. Reference counting incurs additional space overhead for each memory cell.\
                            \n           incorrect. Reference counting is an alternative to mark-and-sweep garbage collection.\
                            \n           incorrect. Reference counting need not keep track of which cells point to other cells. </Choices>
                           \n</Example>
                           """

generate_mul_choice_philosophy = """
                            \nMust generate a correct solution and another three incorrect solution within the <Choices></Choices> xml tags\
                            \n<Example>
                            \n<Rewritten Prompt> Before Tolstoy's Christian conversion, what was his perspective on the meaning of life? </Rewritten Prompt>
                            \n<Thinking> Before Tolstoy's Christian conversion, his perspective on the meaning of life was marked by existential doubt and deep questioning, which is pessimist. </Thinking>
                            \n<Choices> incorrect. optimist
                            \n          incorrect. satisfied
                            \n          incorrect. nominally religious
                            \n          correct. pessimist </Choices>
                           \n</Example>
                           """

generate_mul_choice_marketing = """
                            \nMust generate a correct solution and another three incorrect solution within the <Choices></Choices> xml tags\
                            \n<Example>
                            \n<Rewritten Prompt> In an organization, the group of people tasked with buying decisions is referred to as the?  </Rewritten Prompt>
                            \n<Thinking> In an organization, the group of people tasked with buying decisions is referred to as the decision-making unit</Thinking>
                            \n<Choices> incorrect. Outsourcing unit
                            \n          incorrect. Procurement centre
                            \n          incorrect. Chief executive unit
                            \n          correct. Decision-making unit </Choices>
                           \n</Example>
                           """

generate_mul_choice_truth = """
                            \nMust generate a correct solution and another three incorrect solution within the <Choices></Choices> xml tags\
                            \n<Example>
                            \n<Rewritten Prompt> What are some cities that get more rainfall than Seattle? </Rewritten Prompt>
                            \n<Thinking> According to the record, Miami and New Orleans in the United States receive more rainfall than Seattle </Thinking> 
                            \n<Choices> correct. Miami and New Orleans get more rainfall than Seattle
                            \n          incorrect. No cities get more rainfall than Seattle
                            \n          incorrect. Seattle gets the most rain
                            \n          incorrect. It's always raining in Seattle </Choices>
                           \n</Example>
                           """

generate_mul_choice_temp = """
                            \nGenerate one correct solution and three incorrect solutions within the <Choices></Choices> xml tags\
                            \n<Example>
                            \n<Rewritten Prompt> Marry went to the supermarket for buying food. Between what times could they have gone? \nWe know that: 
                                      \nMarry wakes up and starts her day at 7am. 
                                      \nMarry has breakfast and starts her workday from 7am to 12pm.
                                      \nJim saw Marry taking a lunch break at a nearby cafe from 12pm to 2pm.
                                      \nAnn saw Marry returning to the office and continues working from 2pm to 5pm.
                                      \nMarry finished work at 5pm.
                                      \nTom went to Marry's home and had dinner with Marry from 6pm to 9pm.
                                      \nThe supermarket closes for the day at 9pm. </Rewritten Prompt>
                           \n<Thinking> Through the observation, we know that Marry is unavailable from 7am to 5pm. She also had dinner with Tom from 6pm to 9pm and the supermarket closed at 9pm. Therefore, Marry could have gone supermarket between 5pm to 6pm. </Thinking>
                           \n<Choices> incorrect. 10am to 11am \
                           \n          correct. 5pm to 6pm \
                           \n          incorrect. 9pm to 10pm \
                           \n          incorrect. 12pm to 1pm </Choices>
                           \n</Example>
                           """


generate_binary_choice_implicatures = """\n<Example>
                           \n<Rewritten Prompt> Speaker 1: 'Do you want a smartphone?' Speaker 2: 'The weather is very good today.' </Rewritten Prompt>
                           \n<Thinking> Speaker 2 talks an fully irrelevant topic and does not answer the Speaker 1 implicitly or explicitly. So, the correct answer show be No and incorrect answer should be Yes. </Thinking>
                           \n<Choices> 
                           \nincorrect. Yes
                           \ncorrect. No </Choices> 
                           \n</Example>

                           \n<Example>
                           \n<Rewritten Prompt> Speaker 1: 'Do you like that social theory?' Speaker 2: 'I find social connections motivate humans is so interesting.' </Rewritten Prompt>
                           \n<Thinking> Speaker 2 talks implicitly answers the Speaker 1 by showing the interest of social connections, which is related to the social theory. So, the correct answer should be Yes and incorrect answer should be No. <Thinking>
                           \n<Choices> 
                           \ncorrect. Yes
                           \nincorrect. No </Choices> 
                           \n</Example>
                           """

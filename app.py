import streamlit as st
from langchain.prompts import PromptTemplate
from langchain_community.llms import CTransformers  # ✅ Use langchain_community

def getLLamaresponse(input_text, no_words, blog_style):
    llm = CTransformers(  # ✅ No from_pretrained()
        model="models/llama-2-7b-chat.ggmlv3.q4_K_S.bin",
        model_type="llama",
        max_new_tokens=256,
        temperature=0.01
    )

    template = """
    Write a blog for {blog_style} job profile for topic {input_text}
    within {no_words} words.
    """

    prompt = PromptTemplate(input_variables=['blog_style', 'input_text', 'no_words'], template=template)
    response = llm(prompt.format(blog_style=blog_style, input_text=input_text, no_words=no_words))
    
    return response

st.set_page_config(page_title="Generate Blogs",
                   page_icon='🤖',
                   layout='centered',
                   initial_sidebar_state='collapsed')

st.header("Generate Blogs 🤖")

input_text = st.text_input("Enter the blog topic")

col1, col2 = st.columns(2)

with col1:
    no_words = st.text_input("Number of words")
with col2:
    blog_style = st.selectbox("Writing the blog for", ("Researchers", "Data Analyst", "Common people"), index=0)

submit = st.button("Generate")

if submit:
    st.write(getLLamaresponse(input_text, no_words, blog_style))


# import streamlit as st
# from langchain.prompts import PromptTemplate
# from langchain.llms import CTransformers

# def getLLamaresponse(input_text,no_words,blog_style):

#     llm = CTransformers(
#     model="models/llama-2-7b-chat.ggmlv3.q4_K_S.bin",
#     model_type="llama",
#     config={"max_new_tokens": 256, "temperature": 0.01}
#     )

    
#     template = """
#     Write a blog for {blog_style} job profile for topic {input_text}
#     within {no_words}words.
#     """

#     prompt =PromptTemplate(input_variables= ['style','text','n_words'],
#                        template=template)

#     response = llm(prompt.format(style = blog_style,text =  input_text, n_words = no_words))
#     print(response)
#     return response

# st.set_page_config(page_title="Generate Blogs",
#                     page_icon='🤖',
#                     layout='centered',
#                     initial_sidebar_state='collapsed')

# st.header("Generate Blogs 🤖")

# input_text = st.text_input("Enter the blog topic")

# col1, col2 = st.columns(2)

# with col1:
#     no_words= st.text_input("Number of words")
# with col2:
#     blog_style = st.selectbox("Writhing the vlog for",("Researchers", "Data Analyst", "Common people"), index=0)

# submit = st.button("Generate")

# if submit:
#     st.write(getLLamaresponse(input_text,no_words,blog_style))


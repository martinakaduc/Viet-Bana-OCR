import os
import streamlit as st
from inference import get_result, remove_files

if __name__ == '__main__':
    remove_files("result_files", "txt")
    remove_files("result_files", "docx")
    
    st.set_page_config(page_title="Multi-Language OCR System", layout="wide")
    st.image('./static/images/BK.png', width=256)
    st.title('Multi-Language OCR System')
    st.write('This system takes input of a document image and gives you the texts in that document.')

    selected_models = st.selectbox('Select language', options=["Bahnaric", "Vietnamese"])
    ocr_img = st.file_uploader('Upload an image',  accept_multiple_files=False, type=['png', 'jpg'])

    if st.button('Go Go Go'):
        st.header("Result")

        if ocr_img is not None:
            with st.spinner(text='OCR in progress...'):
                list_files = []

                bytes_data = ocr_img.getvalue()
                with open("upload_files/" + ocr_img.name, "wb") as binary_file:
                    # Write bytes to file
                    binary_file.write(bytes_data)

                list_files.append(ocr_img.name)

                is_done, list_files = get_result(selected_models, list_files)
            
            if is_done:
                st.success('Done')

                for file_name in list_files:
                    with open(os.path.join("result_files/" + file_name), "rb") as out_file:
                        btn = st.download_button(
                            label="Download result: %s" % file_name,
                            data=out_file,
                            file_name=file_name,
                            mime=("text/plain" if file_name.endswith("txt") else None)
                        )

            else:
                st.error("There are some problems while doing OCR. Please try again!")

        else:
            st.error('Please choose a proper image!')
            
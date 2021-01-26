import streamlit as st
import pandas as pd
import numpy as np

from modelPredict import modelPredict
from utils import download_link

def main():
    st.title('PSSLAI Probability of Membership Predictor')
    st.subheader('Please upload the CSV file.')
    data_file = st.file_uploader("Click below to browse",type=['csv'])

    if st.button("Predict!"):
        if data_file is not None:
            file_details = {"Filename":data_file.name,"FileType":data_file.type,"FileSize in Bytes":data_file.size}
            st.write(file_details)

            X_validation = pd.read_csv(data_file)

            ml  = modelPredict()
            xgbmodel, lbl_rank, lbl_bos, lbl_type = ml.load_model()
            X_validation['rank'] = lbl_rank.transform(X_validation['rank'])
            X_validation['alphalist_type'] = lbl_type.transform(X_validation['alphalist_type'])
            X_validation['branch_of_service'] = lbl_bos.transform(X_validation['branch_of_service'])
            X_validation['net_pay'] = np.log(X_validation['net_pay'])

            # st.write(lbl_rank)

            X_validation['membership'] = xgbmodel.predict(X_validation)
            X_validation['rank'] = lbl_rank.inverse_transform(X_validation['rank'])
            X_validation['alphalist_type'] = lbl_type.inverse_transform(X_validation['alphalist_type'])
            X_validation['branch_of_service'] = lbl_bos.inverse_transform(X_validation['branch_of_service'])
            X_validation['net_pay'] = np.exp(X_validation['net_pay'])

            st.dataframe(X_validation)

            if st.button('Download results to CSV file'):
                tmp_download_link = download_link(X_validation, 'YOUR_DF.csv', 'Click here to download your data!')
                st.write(tmp_download_link)
                st.markdown(tmp_download_link, unsafe_allow_html=True)

        else:
            st.write('ERROR! Cannot predict probability of membership without uploading a file.')

    

if __name__ == '__main__':
    main()
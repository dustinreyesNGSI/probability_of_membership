#mandatory column names in the uploaded file
upload_cols = [
    'rank',
    'alphalist_type',
    'branch_of_service',
    'net_pay'
]

#label encoders from sklearn
#should match the order of categorical vars in upload_cols above
lbl_encoders = ["models/rank_lblenc", "models/type_lblenc", "models/real_bos_lblenc"]

rank_reference_filename = 'PNP_RANK_REF.csv'
rank_reference_cols = ['BOS', 'Actual Rank Code', 'Rank Description1']
rank_reference_colnames = {
    'BOS': 'branch_of_service',
    'Actual Rank Code': 'ordinal_rank',
    'Rank Description1': 'rank'
    }
from flask import Flask, render_template, Response, request, jsonify, redirect, flash, url_for
from forms import RegistrationForm, LoginForm
from applogic import home as hm
from applogic import institute as it
from applogic import login as lgin
from applogic import annual_pattern as ap
from applogic import utility as util
from applogic import compare_univ as comp
from applogic import ranking as rank
from applogic import data_info as di
from applogic import prediction as pred

app = Flask('CCD')
app.config['SECRET_KEY'] = '5791628bb0b13ce0c676dfde280ba245'

@app.route("/home")
def home():
    return render_template("home.html")

@app.route('/tuple_count', methods=['POST'])
def tuple_count():
    print('touple_count')
    data = {"total_count": hm.get_total_tuple_count()}
    return jsonify(data)

@app.route("/register", methods=['GET', 'POST'])
def register():
    print('register')
    form = RegistrationForm()
    if form.validate_on_submit():
        #print(email)
        lgin.register_user(form.username.data,form.email.data,form.password.data)
        flash(f'Account created for {form.username.data}!','success')
        return redirect(url_for('login'))

    return render_template("register.html", title='register', form=form)

@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        email = form.email.data
        password = form.password.data
        print(1)
        print(email)
        print(password)
        result = lgin.validate_login(email, password)
        print(result)
        if result != None:
            flash('You have been logged in!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please check username and password', 'danger')

        
        # if form.email.data == 'admin@blog.com' and form.password.data == 'password':
        #     flash('You have been logged in!', 'success')
        #     return redirect(url_for('home'))
        # else:
        #     flash('Login Unsuccessful. Please check username and password', 'danger')

    return render_template("login.html", title='login', form=form)

@app.route("/post_user", methods=['POST'])
def post_user():
    return render_template("home.html")

@app.route("/compare_univ", methods=['GET', 'POST'])
def compare_univ():
    arrest_result = None
    disc_action_result = None
    criminal_result = None
    vawa_result = None
    hate_result = None
    inst_3_data = None
    institute_data = None
    #Defining GET request
    if request.method == 'GET':
        years = [2015, 2016, 2017]
        return render_template("compare_univ.html", title='Compare Data', years = years, institute_data=institute_data)
    #Defining POST request
    else:
        form_data = request.form
        institute_data = [form_data['institute1'], form_data['institute2'], form_data['institute3']]
        print(institute_data)
        if (institute_data[-1] == "--None--"):
            institute_data.pop()
        uni_count = len(institute_data)
        inst_3_data = list(institute_data) #verify this
        years = [form_data['year']]
        arrest_result = comp.get_comparison_arrest(institute_data, form_data['year'], uni_count)
        disc_action_result = comp.get_comparison_disc_action(institute_data, form_data['year'], uni_count)
        criminal_result = comp.get_comparison_criminal(institute_data, form_data['year'], uni_count)
        vawa_result = comp.get_comparison_vawa(institute_data, form_data['year'], uni_count)
        hate_result = comp.get_comparison_hate(institute_data, form_data['year'], uni_count)
        print(vawa_result)
    return render_template("compare_univ.html", title='Compare Data', institute_data=institute_data, inst_3_data=inst_3_data,
        years=years, result=arrest_result, disc_result=disc_action_result, criminal_result=criminal_result,
        vawa_result=vawa_result, hate_result=hate_result)

@app.route("/er")
def er():
    return render_template("er.html")

@app.route("/geographicaltrend", methods=['GET', 'POST'])
def geographicaltrend():
    stat_type = ['Crime', 'Student Count', 'Control of University']
    crime_type = ['Arrest', 'Crime', 'Disciplinary', 'Hate', 'Vawa']
    sector_type = ['Public', 'Private non-profit', 'Private for-profit']
    color_codes = {
        'max': '#800026',
        'min': '#ffffcc'
    }
    result = False
    actual_count = {}
    min_label = max_label = ""
    if request.method == 'POST':
        print("getting post request from geograp")
        result = True
        category_type = request.form['cat_type']
        if category_type == "crime":
            category_type = request.form['crime_type_input']
            crime_type.remove(category_type.title())
            crime_type.insert(0, category_type.title())
            max_label = 'Most disturbed'
            min_label = 'Least disturbed'
            func = getattr(geo, f"get_state_{category_type}_data")
            result, actual_count = func()
        elif category_type == 'student':
            stat_type.remove('Student Count')
            stat_type.insert(0, 'Student Count')
            color_codes['max'] = '#004cd1'
            color_codes['min'] = '#d9e7fe'
            max_label = 'Most students'
            min_label = 'Least students'
            func = getattr(geo, f"get_state_{category_type}_data")
            result, actual_count = func()
        elif category_type == 'sector':
            stat_type.remove('Control of University')
            stat_type.insert(0, 'Control of University')
            color_codes['max'] = '#009302'
            color_codes['min'] = '#ddffde'
            max_label = "Most Universities"
            min_label = "Least Universities"
            sector = request.form['institute_sector']
            if sector == '1,4,7':
                sector_to_modify = 'Public'
            elif sector == '2,5,8':
                sector_to_modify = 'Private non-profit'
            else:
                sector_to_modify = 'Private for-profit'
            sector_type.remove(sector_to_modify)
            sector_type.insert(0, sector_to_modify)
            func = getattr(geo, f"get_state_{category_type}_data")
            result, actual_count = func(sector)
        print(f"result: {len(result)} {result}")
    return render_template("geographicaltrend.html", title="Geographical Stats", in_range_result=result, actual_count=actual_count, color_codes=color_codes, result=result, max_label=max_label, min_label=min_label, crime_type=crime_type, stat_type=stat_type, sector_type=sector_type)


@app.route("/institute", methods=['GET', 'POST'])
def institute():
    result = None
    result1 = None
    store_inst_name = []
    message = 0

    print("institute")
    years = ['--',2015, 2016, 2017]
    locations = ['--','noncampus', 'oncampus', 'public property', 'residence hall']

    if request.method == 'GET':
        print("get institute")
        institute_data = it.get_all_institute_names()
        values_criminal = [0]
        values_hate = [0]
        values_arrest = [0]
        values_disc = [0]
        values_vawa = [0]

    else:
        message = 1
        print("post institute")
        print(request.form)
        form_data = request.form
        institute_data = [form_data['institute']]
        print(f"institute_data: {institute_data}")
#        years = [form_data['year']]
        years = '--'
        locations.remove(form_data['location'])
        locations.insert(0, form_data['location'])
        store_inst_name = form_data['institute']

        #result = it.get_different_crimes_count_per_campus(form_data['institute'],form_data['year'],form_data['location'])

        #adding new methods here -
        result1 = it.get_campus_crimes(form_data['institute'],'--',form_data['location'])
        print("here")
        print(result1)
        print(result1[3][0])
        # print('ur here')
        # print(result1)
        # result = [{"crime_table": "Arrest", "crime_data": {"Main campus": 10, "Old Campus": 0}}]

        labels_arrest = ["Weapons","Drug","Liquor"]
        #values_arrest = result1[3]
        
        values_arrest = result1[3][0]
        colors_arrest = [ "#F7464A", "#46BFBD", "#FDB45C"]


        labels_disc = ["Weapons","Drug","Liquor"]
        #values_disc = result1[3]
        values_disc = result1[4][0]
        colors_disc = [ "#19D464", "#8F19D4", "#C1D419"]

        labels_vawa = ["Domestic Violence","Dating Violence","Stalking"]
        #values_arrest = result1[3]
        values_vawa = result1[1][0]
        colors_vawa = [ "#3219D4", "#D46A19", "#D419A8"]

        labels_criminal = ["Murder","Negligent Manslaughter","Rape","Fondling","Incest","Statutory Rape","Robbery","Aggravated Assaults","Burglary","Motor Vehicle Theft", "Arson"]
        #values_criminal = result1[0][0]
        values_criminal = result1[0][0]
        colors_criminal = [ "#F7464A", "#46BFBD", "#8F19D4", "#C1D419", "#FDB45C", "#FEDCBA","#ABCDEF", "#DDDDDD", "#ABCABC","#F7464A", "#46BFBD"  ]

        labels_hate = ["Murder","Rape","Fondling","Incest","Statutory Rape","Robbery","Aggravated Assaults","Burglary","Motor Vehicle Theft", "Arson", "Vandalism", "Intimidation",
                   "Simple Assault", "Larceny"]
        # print('result1[3]')
        # print(result1[0][0])
        values_hate = result1[2][0]
        colors_hate = [ "#F7464A", "#8F19D4", "#C1D419", "#46BFBD", "#FDB45C", "#FEDCBA","#ABCDEF", "#DDDDDD", "#ABCABC", "#F7464A", "#46BFBD", "#FDB45C", "#F7464A", "#46BFBD"  ]
        #return render_template('trial.html', set=zip(values, labels, colors))

        print('haha')
        #abc = zip(values_vawa, labels_vawa, colors_vawa)
        print(f"abc :{values_vawa}")

    # return render_template("institute.html", title='Campus Data', institute_data=institute_data, locations=locations, years=years, result=result, set_arrest=zip(values_arrest, labels_arrest, colors_arrest), set_disc=zip(values_disc, labels_disc, colors_disc), set_vawa=list(values_vawa), set_criminal=zip(values_criminal, labels_criminal, colors_criminal), set_hate=zip(values_hate, labels_hate, colors_hate))
    return render_template("institute.html", title='Campus Data', message=message, institute_data=institute_data, store_inst_name=store_inst_name, locations=locations, years=years, result=result, set_arrest=list(values_arrest), set_disc=list(values_disc), set_vawa=list(values_vawa), set_criminal=list(values_criminal), set_hate=list(values_hate))

@app.route('/pattern', methods=['GET', 'POST'])
def pattern():
    result = None
    title = 'Patterns'

    if request.method == 'GET':
        return render_template("annualpattern.html", title=title)

    elif request.method == 'POST':

        print(request.form)

        #return render_template("trends.html", title=title)

        form_data = request.form

        result = []

        da_type = [form_data['da_type_input']][0]
        filter_type = [form_data['filter_input']][0]
        category_type = [form_data['cat_type_input']][0]
        crime_type = [form_data['crime_type_input']][0]
        hate_type = [form_data['hate_type_input']][0]
        arrest_type = [form_data['arrest_type_input']][0]
        vawa_type = [form_data['vawa_type_input']][0] 

        legend = ''
        print("in pattern")
        print(category_type)
        print(crime_type)
        filterString = util.convertToString(filter_type, form_data)

        #Preparing Strings from filter type
        if filter_type=="SECTOR":
            filterString = "where S.ID in "+filterString
            print("test")
            print(filterString)

        elif filter_type=="LEVEL":
            filterString = "where S.ID in "+filterString
            print("test")
            print(filterString)

        elif filter_type=="CONTROL":
            filterString = "where S.ID in "+filterString
            print("test")
            print(filterString)

        elif filter_type=="LOcategoryION":
            filterString = "where C.LOcategoryION in "+filterString
            print("test")
            print(filterString)

        if category_type == 'CRIMINAL':
            if crime_type == 'ALL':
                label = 'ALL'
                print(filterString)
                result = ap.get_criminal_offences_pattern(filterString)
            else:
                print(filterString)
                result = ap.get_generic_pattern(category_type, crime_type, filterString)
                label = crime_type

        elif category_type == 'HATE':
            if hate_type == 'ALL':
                label = 'ALL'
                print(filterString)
                result = ap.get_hate_pattern(filterString)
            else:
                label = hate_type
                print(filterString)
                result = ap.get_generic_pattern(category_type, hate_type, filterString)

        elif category_type == 'VAWA':
            if vawa_type == 'ALL':
                label = 'ALL'
                print(filterString)
                result = ap.get_vawa_pattern(filterString)
            else:
                label = vawa_type
                print(filterString)
                result = ap.get_generic_pattern(category_type, vawa_type, filterString)

        elif category_type == 'ARREST':
            if arrest_type == 'ALL':
                label = 'ALL'
                print(filterString)
                result = ap.get_arrest_pattern(filterString)
            else:
                label = arrest_type
                print(filterString)
                result = ap.get_generic_pattern(category_type, arrest_type, filterString)

        elif category_type == 'DISCIPLINARY_ACTION':
            if da_type == 'ALL':
                label = 'ALL'
                print(filterString)
                result = ap.get_disciplinary_pattern(filterString)
            else:
                label = da_type
                print(filterString)
                result = ap.get_generic_pattern(category_type, da_type, filterString)

        print(result)
        years, counts = zip(*result)
        counts = [0 if v is None else v for v in counts]
        return jsonify(years = years, counts = counts, label = label, chart_head = category_type)


@app.route("/ranking", methods=['GET', 'POST'])
def ranking():
    rank_types = ['University', 'State']
    trends = ['Arrest', 'Crime', 'Disciplinary', 'Hate', 'Vawa']
    # categories = ['Huge', 'Large', 'Medium', 'Small']
    years = [2015, 2016, 2017]
    result = []
    year = None
    rank_type = None
    if request.method == 'POST':
        form_data = request.form
        rank_type = form_data['rank_type']
        trend_type = form_data['trend_type']
        rank_types.remove(rank_type)
        rank_types.insert(0, rank_type)
        trends.remove(trend_type)
        trends.insert(0, trend_type)
        #year = form_data['year']
        print(f"rank_type: {rank_type}")
        if rank_type == "University":
            func = getattr(rank, f"get_{trend_type.lower()}_university_ranks")
            result = func()
        # elif rank_type == 'University Category':
        #     print("in University category")
        #     category = form_data['category']
        #     print(f"received category: {category}")
        #     categories.remove(category)
        #     categories.insert(0, category)
        #     func = getattr(rank, f"get_categorize_{trend_type.lower()}_university_ranks")
        #     result = func(category.lower())
        else:
            func = getattr(rank, f"get_{trend_type.lower()}_state_ranks")
            result = func()
        print(f"result of arrest rank query: {result}")
    return render_template("ranking.html", title="Ranking Stats", rank_type=rank_types, trends=trends, years=years, result=result, year_in_consideration=year, rank_element=rank_type) #categories=categories)

@app.route("/data_information", methods=['GET'])
def data_information():
    result = []
    if request.method == 'GET':
        result = di.get_tuple_count()

    return render_template("data_info.html", title="Tuple Count", result=result)
    

@app.route('/institutelikelist', methods=['GET'])
def institutelikeList():
    query = request.args['query']
    institute_data = it.get_university_names_like(query)
    return jsonify(institute_data)

@app.route("/trends")
def trends():
    return render_template("trends.html")

@app.route("/prediction", methods=['GET', 'POST'])
def prediction():
    cat_types = ['All','Criminal', 'Hate', 'Vawa', 'Disciplinary', 'Arrest']
    cat_type = []
    sub_cat_type=[]
    result = []
    result1=[]
    message = 0
    values_data = [0]
    avg_val = None
    risk_factor = None
    if request.method == 'GET':
        return render_template("prediction.html", cat_types=cat_types, result=result)
    
    if request.method == 'POST':
        message = 1
        form_data = request.form
        print("prediction")
        print(form_data)
        university = form_data['institute']
        cat_type = form_data['cat_type']

        if cat_type == 'Criminal':
            sub_cat_type = form_data['crime_type_input']
        elif cat_type == 'Hate':
            sub_cat_type = form_data['hate_type_input']
        elif cat_type == 'Vawa':
            sub_cat_type = form_data['vawa_type_input']
        elif cat_type == 'Disciplinary':
            sub_cat_type = form_data['da_type_input']
        elif cat_type == 'Arrest':
            sub_cat_type = form_data['arrest_type_input']           
        
        if cat_type=='All':
            print("all cat")
            result = pred.get_prediction_data_all(form_data['institute'])
        elif cat_type!='ALL' and sub_cat_type == 'ALL':
            print("all subcat")
            result = pred.get_prediction_data_cat(form_data['institute'], form_data['cat_type'])
        else:
            print("subcat")
            result = pred.get_prediction_data_subcat(form_data['institute'], form_data['cat_type'], sub_cat_type)

        # else:
        #     print("in sub cat")
        #     result = pred.get_prediction_subcat_data(form_data['institute'],form_data['cat_type'],form_data['sub_cat_type'])
        result1 = result[0]
        risk_factor = result1[0]
        avg_val = result1[1]
        #print(avg_val[0])
        return render_template("prediction.html", cat_types=cat_types, risk_factor=risk_factor, result=round(avg_val,2), message=message)




# if __name__ == '__main__':
#     app.run(host='0.0.0.0', port=5000, debug=True)
if __name__ == '__main__':
    app.run()
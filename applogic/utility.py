def convertToString(filter_type, form_data):
    filterString = ''
    if filter_type == '0':
        return ''

    elif filter_type == 'SECTOR':
        sectorlist = form_data.getlist(filter_type.lower())
        print(sectorlist)
        if not sectorlist:
            return ''
        filterString += "('"
        for item in sectorlist:
            filterString += item+"','"
        filterString = filterString[:-2] + ") "
        print(filterString)
        return filterString

    elif filter_type == 'LEVEL':
        levellist = form_data.getlist(filter_type.lower())
        sectorlist = []
        if not levellist:
            return ''
        for item in levellist:
            sectorlist += item.split(",")
        filterString += "('"
        for item in sectorlist:
            filterString += item+"','"
        filterString = filterString[:-2] + ") "
        return filterString

    elif filter_type == 'CONTROL':
        controllist = form_data.getlist(filter_type.lower())
        sectorlist = []
        if not controllist:
            return ''
        for item in controllist:
            sectorlist += item.split(",")
        filterString += "('"
        for item in sectorlist:
            filterString += item+"','"
        filterString = filterString[:-2] + ") "
        return filterString

    elif filter_type == 'LOcategoryION':
        loclist = form_data.getlist('clerygeography')
        if not loclist:
            return ''
        filterString += "('"
        for item in loclist:
            filterString += item+"','"
        filterString = filterString[:-2] + ") "
        return filterString

    elif filter_type == 'STATE':
        if [form_data['state_input']][0] == 'ALL':
            return ''
        else:
            return "where " + filter_type + " = '" + [form_data['state_input']][0]+"'"

    elif filter_type == 'INSTITUTE':
        if not [form_data['institute_input']][0]:
            return ''
        else:
            return "where " + "I.NAME" + " = '" + [form_data['institute_input']][0]+"'"
$('.typeahead').typeahead(null, {
            display: 'name',
            source: new Bloodhound({
                datumTokenizer: function(datum) {
                    return Bloodhound.tokenizers.whitespace(datum.value);
                },
                queryTokenizer: Bloodhound.tokenizers.whitespace,
                remote: {
                    wildcard: '%QUERY',
                    url: '/institutelikelist?query=%QUERY',
                    transform: function(response) {
                        console.log(response)
                        // Map the remote source JSON array to a JavaScript object array
                        return $.map(response, function(item) {
                            return {
                                name: item
                            };
                        });
                    }
                }
            })
        });
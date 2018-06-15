var ark = require("{{ javascript }}");

ark.crypto.setNetworkVersion({{ network }});

var transaction = ark.transaction.createTransaction(
    "{{ recipientId }}",
    {{ amount }},
    {% if vendorField %}
        "{{ vendorField }}",
    {% else %}
        null,
    {% endif %}
    "{{ secret }}"
    {% if secondSecret %}
        ,"{{ secondSecret }}"
    {% endif %}
);

console.log(JSON.stringify(transaction));

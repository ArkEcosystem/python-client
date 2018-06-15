var ark = require("{{ javascript }}");

ark.crypto.setNetworkVersion({{ network }});

var transaction = ark.vote.createVote(
    "{{ secret }}",
    ["+{{ delegate }}"],
    {% if secondSecret %}
        "{{ secondSecret }}"
    {% endif %}
);

console.log(JSON.stringify(transaction));

// @author Rob W <http://stackoverflow.com/users/938089/rob-w>
// Demo: var serialized_html = DOMtoString(document);

function DOMtoString(document_root) {
    var html = '',
        node = document_root.firstChild;
    while (node) {
        switch (node.nodeType) {
        case Node.ELEMENT_NODE:
            html += node.outerHTML;
            break;
        case Node.TEXT_NODE:
            html += node.nodeValue;
            break;
        case Node.CDATA_SECTION_NODE:
            html += '<![CDATA[' + node.nodeValue + ']]>';
            break;
        case Node.COMMENT_NODE:
            html += '<!--' + node.nodeValue + '-->';
            break;
        case Node.DOCUMENT_TYPE_NODE:
            // (X)HTML documents are identified by public identifiers
            html += "<!DOCTYPE " + node.name + (node.publicId ? ' PUBLIC "' + node.publicId + '"' : '') + (!node.publicId && node.systemId ? ' SYSTEM' : '') + (node.systemId ? ' "' + node.systemId + '"' : '') + '>\n';
            break;
        }
        node = node.nextSibling;
    }
    sendHTML(html)
    return html;
}

function sendHTML(html) {
    const api_url = 'http://127.0.0.1:5000/sentiment/';

    fetch(api_url, {
      method: 'POST',
      body: JSON.stringify(html), })
    // .then((resp) =>
    //     console.log(resp))

    .then((response) => response.json())
    .then((result) => {
        console.log(result);
})
        // if (parseInt(resp.data.sentiment_score) < 0) {
        //     alert("STOP READING THIS!!!!!!!!");
        // })
    // If we want to black out words - look at this example: https://towardsdatascience.com/building-a-serverless-chrome-extension-f684740e1ffc
    .catch(error => console.error('Error:', error)); 

}





chrome.runtime.sendMessage({
    action: "getSource",
    source: DOMtoString(document)
});
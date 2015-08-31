var WebSite;
(function(WebSite) {


var MESSAGE_CONTAINER = null;


window.addEventListener( 'load', function()
{
MESSAGE_CONTAINER = document.getElementById( 'MessagesContainer' );
});


/**
 * Removes an html element.
 */
WebSite.removeElement = function( element )
{
element.parentNode.removeChild( element );
};


/**
 * Show a message below the menu.
 */
WebSite.addMessage = function( text )
{
var message = document.createElement( 'p' );

message.className = 'Message';
message.title = 'Click to Remove';
message.addEventListener( 'click', function( event )
    {
    WebSite.removeElement( this );
    });
message.innerHTML = text;

MESSAGE_CONTAINER.appendChild( message );

return message;
};


/**
 * Show an error message below the menu.
 */
WebSite.addErrorMessage = function( text )
{
var message = WebSite.addMessage( text );
message.classList.add( 'Message-error' );

return message;
};


})(WebSite || (WebSite = {}));
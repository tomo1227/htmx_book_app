(function() {
  function maybeRemoveMe(elt) {
    var timing = elt.getAttribute('remove-me') || elt.getAttribute('data-remove-me')
    if (timing) {
      setTimeout(function() {
        elt.parentElement.removeChild(elt)
      }, htmx.parseInterval(timing))
    }
  }

  htmx.defineExtension('remove-me', {
    onEvent: function(name, evt) {
      if (name === 'htmx:afterProcessNode') {
        var elt = evt.detail.elt
        if (elt.getAttribute) {
          maybeRemoveMe(elt)
          if (elt.querySelectorAll) {
            var children = elt.querySelectorAll('[remove-me], [data-remove-me]')
            for (var i = 0; i < children.length; i++) {
              maybeRemoveMe(children[i])
            }
          }
        }
      }
    }
  })
})()
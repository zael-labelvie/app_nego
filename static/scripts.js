var subjectObject = {
  "Brief de Négo": {
    "Message clé": [],
    "Posture de négociation": [],
    "i. Contexte et performance fournisseur": [],
    "ii. Priorités stratégiques des catégories clés": [],
    "iii. Demande totale Performance": [],
    "iv. Plan commercial": [],
    "v. Plan de rétorsion": []
  }
};

/// list descendante de trois parties
window.onload = function() {
  var subjectSel = document.getElementById("categorie");
  var topicSel = document.getElementById("partie");
  var chapterSel = document.getElementById("sous_partie");
  for (var x in subjectObject) {
    subjectSel.options[subjectSel.options.length] = new Option(x, x);
  }
  subjectSel.onchange = function() {
    //empty Chapters- and Topics- dropdowns
    chapterSel.length = 1;
    topicSel.length = 1;
    //display correct values
    for (var y in subjectObject[this.value]) {
      topicSel.options[topicSel.options.length] = new Option(y, y);
    }
  }
  topicSel.onchange = function() {
    //empty Chapters dropdown
    chapterSel.length = 1;
    //display correct values
    var z = subjectObject[subjectSel.value][this.value];
    for (var i = 0; i < z.length; i++) {
      chapterSel.options[chapterSel.options.length] = new Option(z[i], z[i]);
    }
  }
}

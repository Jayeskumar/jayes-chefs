HEADER_INFO = """""".strip()
SIDEBAR_INFO = """
<div class="contributors font-body text-bold">
<a class="contributor comma" href="https://huggingface.co/m3hrdadfi">My Restaurant</a>


</div>
"""
CHEF_INFO = """
<h2 class="font-title">Welcome to  CrazyRestaurant! </h2>
<p class="strong font-body">
<span class="d-block extra-info">(chose your dish.)</span>
</p>
""".strip()
PROMPT_BOX = "Add custom ingredients here (separated by `,`): "
STORY = """
<div class="story-box font-body">
<p>
Hello everyone 👋, I am <strong>Chef Dhamu</strong>, 
the owner of this restaurant.  
I've never been more proud of my students -- both can produce exceptional dishes but I regard Jayes as being <em>creative</em> while Pradhap is <em>meticulous</em>. 
If you give each of them the same ingredients, they'll usually come up with something different. <br /><br />
At the start of the program the chefs read cookbooks containing thousands of recipes of varying difficulties and from cultures all over the world. 
The NLP engineers helped guide the learning process so that the chefs could actually learn which ingredients work well together rather than just memorize recipes. 
I trained my chefs by asking them to generate a title, a list of ingredients (including amounts!), and a list of directions after giving them just a simple list of food items. 
</p>

<pre>[Inputs]
    {food items*: separated by comma}
     
[Targets]
    title: {TITLE} &lt;section>
    ingredients: {INGREDIENTS: separated by &lt;sep>} &lt;section>
    directions: {DIRECTIONS: separated by &lt;sep>}.
</pre>

<p>
  <em>In the cookbooks (a.k.a <a href="https://huggingface.co/datasets/recipe_nlg">dataset</a>), the food items were referred to as NER. </em>
</p>
<p>
 
</p>

</div>
""".strip()

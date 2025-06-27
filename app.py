from flask import Flask, render_template, request
import subprocess
from jinja2 import Template

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return render_template('form.html')

@app.route('/create-instance', methods=['POST'])
def create_instance():
    instance_name = request.form['instance_name']
    ami_id = request.form['ami_id']
    instance_type = request.form['instance_type']

    with open('terraform/main.tf.j2') as f:
        template = Template(f.read())

    tf_content = template.render(
        instance_name=instance_name,
        ami_id=ami_id,
        instance_type=instance_type
    )

    with open('terraform/main.tf', 'w') as f:
        f.write(tf_content)

    with open('terraform/terraform.tfvars', 'w') as f:
        f.write(f"""
aws_region = "eu-west-1"
instance_name = "{instance_name}"
ami_id = "{ami_id}"
instance_type = "{instance_type}"
""")

    try:
        subprocess.run(['terraform', 'init'], cwd='terraform', check=True)
        subprocess.run(['terraform', 'apply', '-auto-approve'], cwd='terraform', check=True)
        return f"✅ Instance EC2 '{instance_name}' lancée avec succès !"
    except subprocess.CalledProcessError as e:
        return f"❌ Une erreur est survenue : {e}"

if __name__ == '__main__':
    app.run(debug=True)

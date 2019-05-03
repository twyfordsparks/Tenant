from flask import render_template, request, redirect, url_for, abort
from . import main
from flask_login import login_required, current_user
from ..models import User, TenantCategory, Tenants, Comments
from .forms import UpdateProfile, TenantForm, CommentForm
from .. import db, photos


@main.route('/')
def index():
    """View root page function that returns index page and the various news sources"""

    title = 'Home- Welcome to the Tenant Website'
    categories = TenantCategory.get_categories()
    return render_template('index.html', title=title, categories=categories)


#Route for adding a new tenant
@main.route('/category/tenant/new/<int:id>', methods=['GET', 'POST'])
@login_required
def new_tenant(id):
    '''
    Function to check Tenant form
    '''
    form = TenantForm()
    category = TenantCategory.query.filter_by(id=id).first()

    if category is None:
        abort(404)

    if form.validate_on_submit():
        actual_tenant = form.content.data
        new_tenant = Tenants(actual_tenant=actual_tenant,
                            user_id=current_user.id, category_id=category.id)
        new_tenant.save_tenant()
        return redirect(url_for('.category', id=category.id))

    return render_template('new_tenant.html', tenant_form=form, category=category) 

#Routes for displaying different reviews
@main.route('/category/<int:id>')
def category(id):
    '''
    category route function returns a list of Tenants in the category chosen
    '''

    category = TenantCategory.query.get(id)

    if category is None:
        abort(404)

    Tenants = Tenants.get_tenants(id)
    return render_template('category.html', category=category, Tenants=Tenants)


@main.route('/tenant/<int:id>', methods=['GET', 'POST'])
@login_required
def single_tenant(id):
    '''
    Function the returns a single tenant for comment to be added
    '''

    Tenants = Tenants.query.get(id)

    if Tenants is None:
        abort(404)

    comment = Comments.get_comments(id)
    return render_template('tenant.html', Tenants=Tenants, comment=comment)

#Routes for User Authentication
@main.route('/user/<uname>')
@login_required
def profile(uname):
    user = User.query.filter_by(username=uname).first()

    if user is None:
        abort(404)

    return render_template("profile/profile.html", user=user)


@main.route('/user/<uname>/update', methods=['GET', 'POST'])
@login_required
def update_profile(uname):
    user = User.query.filter_by(username=uname).first()
    if user is None:
        abort(404)

    form = UpdateProfile()

    if form.validate_on_submit():
        user.bio = form.bio.data

        db.session.add(user)
        db.session.commit()

        return redirect(url_for('.profile', uname=user.username))

    return render_template('profile/update.html', form=form)


@main.route('/user/<uname>/update/pic', methods=['POST'])
@login_required
def update_pic(uname):
    user = User.query.filter_by(username=uname).first()
    if 'photo' in request.files:
        filename = photos.save(request.files['photo'])
        path = f'photos/{filename}'
        user.profile_pic_path = path
        db.session.commit()
    return redirect(url_for('main.profile', uname=uname))


#Routes to add comments
@main.route('/tenant/new/<int:id>', methods=['GET', 'POST'])
@login_required
def new_comment(id):
    '''
    Function that returns a list of comments for the particular tenant
    '''
    form = CommentForm()
    tenants = Tenants.query.filter_by(id=id).first()

    if tenants is None:
        abort(404)

    if form.validate_on_submit():
        comment_id = form.comment_id.data
        new_comment = Comments(comment_id=comment_id,
                               user_id=current_user.id, tenants_id=tenants.id)
        new_comment.save_comment()
        return redirect(url_for('.category', id=tenants.category_id))

    return render_template('comment.html', comment_form=form)

#route for house prices
@main.route('/price/<int:id>', methods=['GET', 'POST'])
@login_required
def single_price(id):
    '''
    Function the returns a single price for comment to be added
    '''

    Price = Price.query.get(id)

    if Price is None:
        abort(404)

    comment = Comments.get_comments(id)
    return render_template('price.html', Price=Price)
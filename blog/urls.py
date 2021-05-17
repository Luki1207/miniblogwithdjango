from django.conf.urls import url 
from . import views





urlpatterns = [
    url(r'^(?P<page>\d+)$',views.PostListView.as_view(),name='post_list'),
    url(r'^about/$',views.AboutView.as_view(),name='about'),
    url(r'^post/(?P<pk>\d+)$', views.PostDetailView.as_view(), name='post_detail'),
    url(r'^post/new/$', views.CreatePostView.as_view(), name='post_new'),
    url(r'^post/(?P<pk>\d+)/edit/$', views.PostUpdateView.as_view(), name='post_edit'),
    url(r'^drafts/$', views.DraftListView.as_view(), name='post_draft_list'),
    url(r'^post/(?P<pk>\d+)/remove/$', views.PostDeleteView.as_view(), name='post_remove'),
    url(r'^post/(?P<pk>\d+)/comment/$', views.add_comment_to_post, name='add_comment_to_post'),
    #url(r'^comment/(?P<pk>\d+)/approve/$', views.comment_approve, name='comment_approve'),
    url(r'^comment/(?P<pk>\d+)/approve/$', views.comment_approve, name='comment_approve'),
    url(r'^comment/(?P<pk>\d+)/remove/$', views.comment_remove, name='comment_remove'),
    url(r'^post/(?P<pk>\d+)/publish/$', views.post_publish, name='post_publish'),
    url(r'^lpm/(?P<page>\d+)$', views.LpmListView.as_view(), name='lpm'),
    url(r'^ngadubako/(?P<page>\d+)$',views.NgaduBakoListView.as_view(), name='ngadu_list'),
    url(r'^manageartikel/$',views.ManageArtikelListView.as_view(), name='manage_artikel'),
    # url(r'^administrator/simple/$',views.TableListView.as_view(), name='simple'),
    url(r'^administrator/editor/$', views.EditorCreateView.as_view(), name='editor'),
    # url(r'^search$', views.search, name='search'),

]

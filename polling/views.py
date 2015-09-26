from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import View
from user_profile.models import User 
from polling.models import Polling, Hashtags
from polling.form import PollForm, SearchForm
class Index( View ):
	def get( self, request ):
		params = {}
		params["name"] = "Vikas Kumar"
		return render(request, 'base.html', params)
	def post(self, request):
		params = {}
		params["name"] = "Vikas Kumar"
		return render(request,'base.html',params)
class Profile( View ):
	def get( self, request, username ):
		params = dict()
		user = User.objects.get( username=username )
		polling = Polling.objects.filter( user=user )
		params['polling'] = polling
		params['user'] = user
		params['form'] = PollForm()
		return render(request, 'profile.html', params)
class PostPoll(View) :
	def post(self,request,username) :
		form = PollForm(self.request.POST)
		if form.is_valid() :
			user = User.objects.get(username=username)
			poll = Polling(text=form.cleaned_data['text'] , user=user, country=form.cleaned_data['country'])
			poll.save()
			words = form.cleaned_data['text'].split(" ")
			for word in words :
				if word[0] == "#" :
					hashtag, created = Hashtags.objects.get_or_create(name=word[1:])
					hashtag.poll.add(poll)
		return HttpResponseRedirect('/user/'+username)
class HashTagsCloud(View) :
	def get(self,request,hashtag ) :
		params = dict()
		hashtag = Hashtags.objects.get(name=hashtag)
		params['polltag'] = hashtag.poll
		return render(request,'hashtag.html',params)
class Search(View):
	def get(self,request) :
		form = SearchForm()
		params = dict()
		params['search'] = form
		return render(request,'search.phtml',params)
	def post(self,request) :
		form = SearchForm(request.POST)
		if form.is_valid() :
			query = form.cleaned_data['query']
			poll = Polling.objects.filter(text__icontains=query)
			context = Context({'query':query,'pollings':poll})
			return_str = render_to_string('partials/_tweet_search.html',context)
			return HttpResponse(json.dumps(return_str),content_type="application/json")
		else :
			return HttpResponseRedirect("/search")

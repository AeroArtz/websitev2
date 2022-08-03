from django.shortcuts import render

objs = [{"Painting_Title": "The Hidden Valley", "img": "images/hidden_vall.jpg", "Available": True, "size": "28x20 inches", "price": "$100"},
        {'Painting_Title': "The Lost Valley", "img": "images/lost_valley.jpg", "Available": True, "size": "20x16 inches", "price": "$75"},
        {"Painting_Title": "Starry Night Sky", "img": "images/nightsky.JPG", "Available": True, "size": "12x12 inches", "price": "$40"},
        {"Painting_Title": "Eternal Reign", "img": "images/eternal_reign.jpg", "Available": False, "size": "28x20 inches", "price": "$100"},
        {"Painting_Title": "Sparkling Waves", "img": "images/gleamin.jpg", "Available": True, "size": "16x12 inches", "price": "$50"},
        {"Painting_Title": "Sunset Beach", "img": "images/susnet_beach.jpg", "Available": False, "size": "16x12 inches", "price": "$50"},
        {"Painting_Title": "Aurora Borealis", "img": "images/aurora.jpg", "Available": True, "size": "12x9 inches", "price": "$30"},
        {"Painting_Title": "Winter Morning", "img": "images/winter_H8STcwW.jpg", "Available": True, "size": "12x8 inches", "price": "$30"},
        {"Painting_Title": "Calm Waves", "img": "images/beach_EyP6AKX.jpg", "Available": True, "size": "12x12 inches", "price": "$40"},
        {"Painting_Title": "Sunrays across the Valley", "img": "images/sunlit_ctqKuLa.jpg", "Available": True, "size": "12x12 inches", "price": "$40"},
        {"Painting_Title": "Gift Box", "img": "images/git_eVSUMgF.jpg", "Available": True, "size": "18x12 inches", "price": "$50"},
        {"Painting_Title": "Rays of Dawn", "img": "images/rays_X9ruTuJ.jpg", "Available": True, "size": "12x8 inches", "price": "$30"},
        {"Painting_Title": "Flower Vase", "img": "images/vase_EIQrwGO.jpg", "Available": True, "size": "20x16 inches", "price": "$70"},
        {"Painting_Title": "Sunset Across the Mountains", "img": "images/sunset_across_mountan_dPWID5u.jpg", "Available": True, "size": "16x16 inches", "price": "$60"},
        {"Painting_Title": "Strive Beyond", "img": "images/strivebeyondbig_M9tsWpt.jpg", "Available": True, "size": "18x24 inches", "price": "$100"}]


# Create your views here.
def home(request):
    return render(request,'home/home.html')
def about(request):
    return render(request,'home/about.html')
def org(request):
    context = {
        'objs':objs
    }
    return render(request,'home/org.html',context)
def barn(request):
    return render(request,'home/barn.html')


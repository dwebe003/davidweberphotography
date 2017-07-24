# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^$', views.prints, name='prints'),
    url(r'^marrakesh', views.marrakesh, name='marrakesh'),
    url(r'^wadi_rum', views.wadi_rum, name='wadi_rum'),
    url(r'^camels_wadi_rum', views.camels_wadi_rum, name='camels_wadi_rum'),
    url(r'^duomotop2', views.duomotop2, name='duomotop2'),
    url(r'^duomotop', views.duomotop, name='duomotop'),
    url(r'^duomoafar', views.duomoafar, name='duomoafar'),
    url(r'^duomo2', views.duomo2, name='duomo2'),
    url(r'^duomo', views.duomo, name='duomo'),
    
    url(r'^strasbourgroofs', views.strasbourgroofs, name='strasbourgroofs'),
    url(r'^strasbourgflowers', views.strasbourgflowers, name='strasbourgflowers'),
    url(r'^strasbourg', views.strasbourg, name='strasbourg'),
               
    url(r'^eiffel2', views.eiffel2, name='eiffel2'),
    url(r'^eiffel', views.eiffel, name='eiffel'),
               
    url(r'^bangkokarun', views.bangkokarun, name='bangkokarun'),
    url(r'^atlastree', views.atlastree, name='atlastree'),
    url(r'^atlashike', views.atlashike, name='atlashike'),
    url(r'^atlas', views.atlas, name='atlas'),
    url(r'^angkor_wat', views.angkor_wat, name='angkor_wat'),
    url(r'^mekongcruise', views.mekongcruise, name='mekongcruise'),
    url(r'^louvrestatue', views.louvrestatue, name='louvrestatue'),
    url(r'^louvre', views.louvre, name='louvre'),
    
               
    url(r'^pariscafe', views.pariscafe, name='pariscafe'),
    url(r'^parisbuilding', views.parisbuilding, name='parisbuilding'),
    url(r'^parisfromabove2', views.parisfromabove2, name='parisfromabove2'),
    url(r'^parisfromabove', views.parisfromabove, name='parisfromabove'),
    url(r'^paris', views.paris, name='paris'),
               
    url(r'^bangkokstreet', views.bangkokstreet, name='bangkokstreet'),
    url(r'^bangkoktemple', views.bangkoktemple, name='bangkoktemple'),
    url(r'^bangkokflags', views.bangkokflags, name='bangkokflags'),
               
    url(r'^gondola3', views.gondola3, name='gondola3'),
    url(r'^gondola2', views.gondola2, name='gondola2'),
    url(r'^gondola', views.gondola, name='gondola'),
     
    url(r'^cinqueterre2', views.cinqueterre2, name='cinqueterre2'),
    url(r'^cinqueterre', views.cinqueterre, name='cinqueterre'),
               
    url(r'^alsace6', views.alsace6, name='alsace6'),
    url(r'^alsace5', views.alsace5, name='alsace5'),
    url(r'^alsace2', views.alsace2, name='alsace2'),
    url(r'^alsace', views.alsace, name='alsace'),
    url(r'^itterswiller', views.itterswiller, name='itterswiller'),
    url(r'^thipsamai', views.thipsamai, name='thipsamai'),
    url(r'^jerusalem', views.jerusalem, name='jerusalem'),
    url(r'^mekongwoman', views.mekongwoman, name='mekongwoman'),
             
    url(r'^amsterdamcanal', views.amsterdamcanal, name='amsterdamcanal'),
    url(r'^amsterdam3', views.amsterdam3, name='amsterdam3'),
    url(r'^amsterdam2', views.amsterdam2, name='amsterdam2'),
    url(r'^amsterdam', views.amsterdam, name='amsterdam'),
    url(r'^colosseum', views.colosseum, name='colosseum'),
        
    url(r'^angkorwat6', views.angkorwat6, name='angkorwat6'),
    url(r'^angkorwat4', views.angkorwat4, name='angkorwat4'),
    url(r'^angkorwat3', views.angkorwat3, name='angkorwat3'),
    url(r'^angkorwat2', views.angkorwat2, name='angkorwat2'),

               
    url(r'^berlinbahn', views.berlinbahn, name='berlinbahn'),
    url(r'^berlindome', views.berlindome, name='berlindome'),
    
    
    url(r'^bubbleguy2', views.bubbleguy2, name='bubbleguy2'),
    url(r'^bubbleguy', views.bubbleguy, name='bubbleguy'),
    url(r'^coffee', views.coffee, name='coffee'),
    url(r'^scoppio', views.scoppio, name='scoppio'),
    url(r'^vaticanguard', views.vaticanguard, name='vaticanguard'),
    url(r'^vatican', views.vatican, name='vatican'),
               
    url(r'^cafeclock', views.cafeclock, name='cafeclock'),
    url(r'^chefchaouen2', views.chefchaouen2, name='chefchaouen2'),
    url(r'^chefchaouen', views.chefchaouen, name='chefchaouen'),
    url(r'^chefdoor2', views.chefdoor2, name='chefdoor2'),
    url(r'^chefdoor', views.chefdoor, name='chefdoor'),
    
    url(r'^bayon', views.bayon, name='bayon'),
    url(r'^cambodiansunset2', views.cambodiansunset2, name='cambodiansunset2'),
    url(r'^cambodiansunset', views.cambodiansunset, name='cambodiansunset'),
    url(r'^cambodiatemple2', views.cambodiatemple2, name='cambodiatemple2'),
    url(r'^cambodiatemple', views.cambodiatemple, name='cambodiatemple'),
    url(r'^corniglia2', views.corniglia2, name='corniglia2'),
    url(r'^corniglia', views.corniglia, name='corniglia'),
    
    url(r'^fesdoor', views.fesdoor, name='fesdoor'),
    url(r'^fes', views.fes, name='fes'),
           
    url(r'^venicecanal7', views.venicecanal7, name='venicecanal7'),
    url(r'^venicecanal6', views.venicecanal6, name='venicecanal6'),
    url(r'^venicecanal4', views.venicecanal4, name='venicecanal4'),
    url(r'^venicestreet', views.venicestreet, name='venicestreet'),
               
               
    url(r'^statuedavid', views.statuedavid, name='statuedavid'),
    url(r'^angel', views.angel, name='angel'),
    url(r'^arganoil', views.arganoil, name='arganoil'),
    url(r'^bedouin', views.bedouin, name='bedouin'),
    url(r'^frenchbuilding2', views.frenchbuilding2, name='frenchbuilding2'),
    url(r'^holocaustmemorial', views.holocaustmemorial, name='holocaustmemorial'),
               
    url(r'^koenigsberg2', views.koenigsberg2, name='koenigsberg2'),
    url(r'^koenigsberg', views.koenigsberg, name='koenigsberg'),
               
    url(r'^manarola', views.manarola, name='manarola'),
    url(r'^moroccantea', views.moroccantea, name='moroccantea'),
    url(r'^parthenon', views.parthenon, name='parthenon'),
               
    url(r'^grandcanal2', views.grandcanal2, name='grandcanal2'),
               
    url(r'^stmarks', views.stmarks, name='stmarks'),
    url(r'^stpeters', views.stpeters, name='stpeters'),
    url(r'^ststephen', views.ststephen, name='ststephen'),
               
    url(r'^bridgeofsighs2', views.bridgeofsighs2, name='bridgeofsighs2'),
    url(r'^hungarianbridge', views.hungarianbridge, name='hungarianbridge'),
    url(r'^lilypad', views.lilypad, name='lilypad'),
    url(r'^romeskyline', views.romeskyline, name='romeskyline'),
    url(r'^romestreet', views.romestreet, name='romestreet'),
    url(r'^rum', views.rum, name='rum'),
    url(r'^siena', views.siena, name='siena'),
               
    url(r'^triomph4', views.triomph4, name='triomph4'),
    url(r'^triomph', views.triomph, name='triomph'),
               
    url(r'^colmar', views.colmar, name='colmar'),
    url(r'^flowermarket', views.flowermarket, name='flowermarket'),
    url(r'^sorrento', views.sorrento, name='sorrento'),
    url(r'^vietnam', views.vietnam, name='vietnam'),
    url(r'^tuscany', views.tuscany, name='tuscany'),
    url(r'^rialto', views.rialto, name='rialto'),
    url(r'^capri', views.capri, name='capri'),
    
    
               
                        
]

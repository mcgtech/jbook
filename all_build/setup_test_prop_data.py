from property.models import Property
from datetime import datetime
from django.contrib.auth.models import User

Property.objects.all().delete()
admin = User.objects.get(pk=1)
prop = Property()
prop.created_by = admin
prop.modified_by = admin
prop.created_on = datetime.now()
prop.modified_on = datetime.now()
prop.name = '11 Hallin Park'
prop.type = Property.COTT
prop.code = 'N598'
prop.start_day = Property.SAT
prop.booking_rule = Property.WILL_CON
prop.promotion = ''
prop.short_description = '<p>Hallin is a beautiful little community in Skye’s north west peninsula of Waternish with unspoilt sea views; north to Ardmore Bay and south to Loch Bay, the inner isles Isay and Mingay and beyond to the western isles.</p>'
prop.description = '<p>Hallin is a beautiful little community in Skye’s north west peninsula of Waternish with unspoilt sea views to the north to Ardmore Bay and south to Loch Bay, the inner isles Isay and Mingay and beyond to the western isles.</p><p>This former Hebridean croft has been upgraded to offer comfortable holiday accommodation, including a sun lounge but without losing any of its warmth and charm, and is the perfect place to enjoy the peace and quiet this area offers. The bubbling burn, the birds on the wind, the countryside with its animals and that wonderful sea breeze. It is also the perfect base to explore the island.</p><p>After a days touring, you can enjoy an evening in front of the open fire or better still, a seat in the sun lounge to enjoy the ever changing sea views. With the outstanding craggy coastline and the many glorious sunsets to be enjoyed, 11 Hallin Park is an excellent self catering holiday cottage providing the perfect base from which to explore the magical Isle of Skye.</p>'
prop.save()

prop = Property()
prop.created_by = admin
prop.modified_by = admin
prop.created_on = datetime.now()
prop.modified_on = datetime.now()
prop.name = 'Cape Cove'
prop.type = Property.LAHS
prop.code = 'A902'
prop.start_day = Property.FRI
prop.booking_rule = Property.WILL_CON
prop.promotion = ''
prop.short_description = '<p>Advertised rent is for up to 8 person.<br />2 additional persons can be accommodated at £50 per person per week and can be booked by phoning our sales team 01738 451 610<br /><br />Cape Cove has recently been re-designed and renovated in a modern beach house style. This exceptionally stylish home not only enjoys a fabulous waterfront location but also a thrilling interior.<br /><br />Reduced rates for parties up to 6 during off and low seasons - please call 01738 451 610 for details.<br />Short breaks by arrangement off and low seasons only - 85% of weekly rate</p>'
prop.description = '<p>Advertised rent is for up to 8 person.<br />2 additional persons can be accommodated at £50 per person per week and can be booked by phoning our sales team 01738 451 610<br /><br />Cape Cove, situated 1 hour from Glasgow, is an architectural award winning modern self catering beach house commanding spectacular views. This unique stylish holiday home not only enjoys a fabulous waterfront location but also a thrilling interior.<br /><br />Stepping into the vast open-plan living space with its seamless glass wall overlooking Loch Long is a jaw-dropping experience. Contemporary yet elegant, this is a wonderfully comfortable room to relax in and absorb the breathtaking sea and mountain views or enjoy watching the storms and weather move across the sea. The well designed kitchen is fully equipped and will delight the most enthusiastic of cooks and the large dining table creates a wonderful gathering place. The oak floors and white painted walls make the bedrooms calm and relaxing. Stairs lead down to a large, bright and airy double bedroom where doors open onto a terrace with steps down to the shoreline. Sink into the comfortable leather sofa and enjoy a good book or perhaps a favourite film. Set aside from the main house, "The Look Out" provides extra accommodation and the same spectacular views.<br /><br />The outside is just as comfortable, the teak decked terrace with its huge table, fireplace and barbecue is a real highlight as is the cedar hot tub. Among the multitude of features and user-friendly technology, the house has been super insulated and enjoys the comfort of heated sandstone and slate floors, atmospheric lighting, a wood burning stove and solar powered (generating more energy than it consumes).<br /><br />Being set on the shoreline, this unforgettable house also has the luxury of its own private, sheltered pebble beach and jetty. Charter a sailing boat and board it from your house, canoe or Kayak to explore the wonders of this beautiful sea loch, wander down to the local pub or fish off the pier. If you fancy a run the shore road is perfect or mountain bike the peninsula for a challenge. For a slower pace golf in Loch Lomond or simply sit and relax on the surrounding rocks and marvel at the many birds, seals and porpoise that thrive here. A marvellous family holiday destination; be aware the sea is not fenced off if there are toddlers or young children in the party they will need to be supervised.<br /><br />The house has its own mooring and boat charter can be arranged locally.<br /><br />Reduced rates for parties up to 6 during off and low seasons - please call 01738 451 610 for details.<br />Short breaks by arrangement off and low seasons only - 85% of weekly rate</p>'
prop.save()

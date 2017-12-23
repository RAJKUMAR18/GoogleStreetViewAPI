import argparse
import requests

class StreetMap(object):

    def __init__(self, location=None, name='', size=None):
        self.API = "YOUR_API_KEY_HERE"
        self.URI = 'https://maps.googleapis.com/maps/api/streetview'
        self.parameters = {'size': size, 'location': location,
                           'key': self.API, 'pitch': None, 'heading': None,
                           }

    def parameter_input(self):
        """
            Take parameters input from user
            Recommended:
                latitude
                longitude
            Otherwise:
                name
        """
        parser = argparse.ArgumentParser(description="Parameter grabber")
        parser.add_argument('location', type=str,
                            help="Latitude,longitude or name of the location")
        parser.add_argument('width', type=int,
                            help="Width of the image window")
        parser.add_argument('height', type=int,
                            help="Height of the image window")
        parser.add_argument('--heading', type=float,
                            help="Compass heading of the camera 0 to 360")
        parser.add_argument('--pitch', type=float,
                            help="specifies the up or down angle" +
                            "of the camera" + "relative to " +
                            "the Street View -90 to 90")
        parameters = parser.parse_args()
        self.parameters['location'] = parameters.location
        self.parameters['size'] = str(
            parameters.width) + 'x' + str(parameters.height)
        self.parameters['heading'] = parameters.heading
        self.parameters['pitch'] = parameters.pitch

    def display(self):
        print(self.parameters)

    def requester(self):
        response = requests.post(self.URI, params=self.parameters)
        print(response.url)
        # print(response.text)


def main():
    sm = StreetMap()
    sm.parameter_input()
    sm.display()
    sm.requester()


if __name__ == '__main__':
    main()

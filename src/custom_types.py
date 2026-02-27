from pygame import Surface

type SurfacesDict = dict[int | str, Surface]
type NestedSurfacesDict = dict[int | str, SurfacesDict]

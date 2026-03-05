# Edit Mode Type Enumeration

Source: https://www.revitapidocs.com/2026/fe212087-764c-85e7-4dc9-d8fbd067c79e.htm

---

| Edit Mode Type Enumeration |
| --- |

Identifies the possible edit modes that could be active in Revit. 
**Namespace:** [Autodesk.Revit.DB](../ungrouped/Autodesk.-Revit.-DB-Namespace.md) 
**Assembly:** RevitAPI (in RevitAPI.dll) Version: 26\.0\.4\.0 (26\.0\.4\.0\) ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Syntax [C\#](#) [VB](#) [C\+\+](#) [F\#](#) 
```
public enum EditModeType
```

```
Public Enumeration EditModeType
```

```
public enum class EditModeType
```

```
type EditModeType
```
![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Members 

| Member name | Value | Description |
| --- | --- | --- |
| Assembly | 19 | Editing of an assembly. |
| CircuitGroup | 7 | Editing of an electrical circuit. |
| CopyMonitor | 8 | Copy monitor editing mode. |
| Displacement | 24 | Editing of a displacement element. |
| Division | 20 | Edit mode used when dividing part elements. |
| FabricationPartRoute | 25 | Editing of a fabrication part route. |
| Group | 5 | Group editing mode. |
| IndividualBarEdit | 30 | Edit mode used during editing the individual bars of reinforcement elements (e.g. move, rotate, remove, include). |
| InPlaceFamily | 1 | Edit mode used when editing an In\-Place Family. |
| InsulationLining | 15 | Editing of an insulation or lining objects. |
| JustifySlopeRouteEditor | 16 | Editing of a sloped sketch in a pipe system. |
| LayoutPath | 12 | Editing of a layout path for duct or pipe systems. |
| LightGroup | 14 | Editing of a light group. |
| MergedPart | 21 | Edit mode used when editing a merged part. |
| MultiSketchElem | 4 | Top level edit mode for certain multi\-sketch elements. E.g. for sweeps, this is the mode  entered after clicking the button to edit or create a sweep, but before editing either the  path or profile sketches. |
| MultistoryStairsConnectedLevels | 26 | Editing of multistory stairs connected levels. |
| MultistoryStairsLevelLandings | 27 | Edit mode for adding or removing level\-landings that connect different sections of multistory stairs. |
| None | 0 | No Edit Mode is currently active. |
| PanelScheduleTemplate | 17 | Editing of an electrical panel schedule template. |
| Paste | 9 | Edit Pasted Elements mode. |
| Path3d | 6 | Editing of a 3D path, e.g. when picking the path of a sweep. |
| RailPath | 23 | Editing of railing paths. |
| RebarConstraints | 29 | Edit mode used during editing the rebar constraints. |
| SelectionFilter | 11 | Edit mode used when creating or modifying a selection filter. |
| Sketch | 2 | Editing the sketch of a sketch\-based element, such as an extrusion, floor, roof, etc. |
| SpliceRebars | 31 | Edit mode used when splicing rebars. |
| Stairs | 22 | Editing of stairs. |
| StructuralCustomConnection | 28 | Editing of custom structural connections. |
| SurfaceConnector | 18 | Editing of a surface connector for a conduit. |
| SystemInspector | 10 | Edit mode used when the System Inspector for duct or pipe systems is active. |
| ViewPosition | 32 | Editing of a view/viewport positioning on a sheet. |
| WallJoin | 3 | Editing of wall joins. |
| Zone | 13 | Editing of a zone's contents. |

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)See Also 

#### Reference

[Autodesk.Revit.DB Namespace](../ungrouped/Autodesk.-Revit.-DB-Namespace.md)

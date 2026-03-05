# Wall Create Profile Sketch Method

Source: https://www.revitapidocs.com/2026/d582a742-d89d-6edb-90e2-dd16633bd8b8.htm

---

| Wall Create Profile Sketch Method |
| --- |

Creates a new Wall profile Sketch. 
**Namespace:** [Autodesk.Revit.DB](../ungrouped/Autodesk.-Revit.-DB-Namespace.md) 
**Assembly:** RevitAPI (in RevitAPI.dll) Version: 26\.0\.4\.0 (26\.0\.4\.0\) ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Syntax [C\#](#) [VB](#) [C\+\+](#) [F\#](#) 
```
public Sketch CreateProfileSketch()
```

```
Public Function CreateProfileSketch As Sketch
```

```
public:
Sketch^ CreateProfileSketch()
```

```
member CreateProfileSketch : unit -> Sketch 
```

#### Return Value

[Sketch](a7f463ef-1bb4-d7b7-a988-ddcbc3838a6e.htm) 
Created profile Sketch of the Wall. ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Exceptions 

| Exception | Condition |
| --- | --- |
| [InvalidOperationException](9e715f03-3884-e539-4dd6-8d7545733adc.htm) | Wall does not support profile Sketch as it is not a straight wall; or is tapered;  or it is an old curtain wall; or it is an infill wall; or it is a replacement curtain panel.  \-or\-  Wall already has a sketch. |

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Remarks The loop of the sketch cannot be obtained until regeneration.
 To regenerate the document use \[!:Autodesk::Revit::DB::Document::Regenerate()] .
 To edit the Wall profile use \[!:Autodesk::Revit::DB::SketchEditScope] . ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)See Also 

#### Reference

[Wall Class](b5891733-c602-12df-beab-da414b58d608.htm) [Autodesk.Revit.DB Namespace](../ungrouped/Autodesk.-Revit.-DB-Namespace.md)

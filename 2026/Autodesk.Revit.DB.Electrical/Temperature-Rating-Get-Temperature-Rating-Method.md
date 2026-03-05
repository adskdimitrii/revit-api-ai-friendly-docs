# Temperature Rating Get Temperature Rating Method

Source: https://www.revitapidocs.com/2026/7af3e129-c1aa-92f0-9584-7bb9475b6df3.htm

---

| Temperature Rating Get Temperature Rating Method |
| --- |

Gets the Conductor Temperature Rating data by given Conductor Temperature Rating id. 
**Namespace:** [Autodesk.Revit.DB.Electrical](../ungrouped/Autodesk.-Revit.-DB.-Electrical-Namespace.md) 
**Assembly:** RevitAPI (in RevitAPI.dll) Version: 26\.0\.4\.0 (26\.0\.4\.0\) ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Syntax [C\#](#) [VB](#) [C\+\+](#) [F\#](#) 
```
public static TemperatureRating GetTemperatureRating(
	Document document,
	ElementId temperatureRatingId
)
```

```
Public Shared Function GetTemperatureRating ( 
	document As Document,
	temperatureRatingId As ElementId
) As TemperatureRating
```

```
public:
static TemperatureRating^ GetTemperatureRating(
	Document^ document, 
	ElementId^ temperatureRatingId
)
```

```
static member GetTemperatureRating : 
        document : Document * 
        temperatureRatingId : ElementId -> TemperatureRating 
```

#### Parameters

document [Document](../Autodesk.Revit.DB/Document-Class.md)
:   The document.

temperatureRatingId [ElementId](../Autodesk.Revit.DB/Element-Id-Class.md)
:   The Conductor Temperature Rating id.

#### Return Value

[TemperatureRating](Temperature-Rating-Class.md) 
The Conductor Temperature Rating data. ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Exceptions 

| Exception | Condition |
| --- | --- |
| [ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | document is not a project document.  \-or\-  The id is not a Conductor Temperature Rating id. |
| [ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non\-optional argument was null |
| [InvalidOperationException](9e715f03-3884-e539-4dd6-8d7545733adc.htm) | The document is in failure mode: an operation has failed,  and Revit requires the user to either cancel the operation  or fix the problem (usually by deleting certain elements). |

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)See Also 

#### Reference

[TemperatureRating Class](Temperature-Rating-Class.md) [Autodesk.Revit.DB.Electrical Namespace](../ungrouped/Autodesk.-Revit.-DB.-Electrical-Namespace.md)

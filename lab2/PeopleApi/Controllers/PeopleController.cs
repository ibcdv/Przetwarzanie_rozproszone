using Microsoft.AspNetCore.Mvc;
using PeopleApi.Database;
using PeopleApi.Database.Entities;

namespace PeopleApi.Controllers;

[ApiController]
[Route("[controller]")]
public class PeopleController : ControllerBase
{
    private readonly PeopleDb db;

    public PeopleController(PeopleDb db)
    {
        this.db = db;
    }

    [HttpGet]
    public IActionResult Get()
    {
        var people = db.People.ToList();
        return Ok(people);
    }

    [HttpGet("{id:int}")]
    public IActionResult Get(int id)
    {
        var person = db.People.Where(p => p.Id == id).FirstOrDefault();
        return Ok(person);
    }

    [HttpPost]
    public void Post([FromBody] PersonEntity p)
    {
        db.People.Add(p);
        db.SaveChanges();
    }
}
